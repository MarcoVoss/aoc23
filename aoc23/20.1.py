from __future__ import annotations
from abc import ABC


MODULES: dict[str, Module] = {}
SIGNALS: list[tuple[str, bool]] = []

class Module(ABC):
    def __init__(self, name: str, targets: list[str]) -> None:
        self.__name = name
        self.__targets = targets
        self._sources = []

    def add_source(self, source: list[str]) -> None:
        self._sources.append(source)

    def get_targets(self) -> list[str]:
        return self.__targets

    def receive(self, source_module: str, input_signal: bool) -> None:
        """if necessary, do something with the signal"""
        pass

    def transmit(self) -> list[tuple[str, bool]]:
        return [
            (self.__name, target, self._create_signal(target))
            for target in self.__targets
        ]
    
    def _create_signal(self, target: str) -> bool:
        """append the output signal logic in here"""
        pass
    
    def __str__(self) -> str:
        return f"{self.__name} -> {', '.join(self.__targets)}"


class Broadcaster(Module):
    input_signal = False

    def receive(self, source_module: str, input_signal: bool) -> None:
        self.input_signal = input_signal

    def _create_signal(self, target: str) -> bool:
        return self.input_signal


class FlipFlop(Module):
    __is_on = False
    __input_signal = False

    def receive(self, source_module: str, input_signal: bool) -> None:
        self.__input_signal = input_signal
        if input_signal is False:
            self.__is_on = not self.__is_on

    def transmit(self) -> list[tuple[str, bool]]:
        if self.__input_signal:
            return []
        return super().transmit()

    def _create_signal(self, target: str) -> bool:
        return self.__is_on


class Conjunction(Module):
    remembered_signals = {}

    def receive(self, source_module: str, input_signal: bool) -> bool:
        self.remembered_signals[source_module] = input_signal
    
    def _create_signal(self, target: str) -> bool:
        return not all(
            self.remembered_signals.get(source, False)
            for source in self._sources
        )


for line in open("aoc23/20.1.txt", 'r').readlines():
    line = line.strip()
    name, targets = line.split(" -> ", 1)
    targets = targets.split(", ")
    if name.startswith("%"):
        MODULES[name[1:]] = FlipFlop(name[1:], targets)
    elif name.startswith("&"):
        MODULES[name[1:]] = Conjunction(name[1:], targets)
    else:
        MODULES[name] = Broadcaster(name, targets)

for name, module in MODULES.items():
    for target in module.get_targets():
        if module := MODULES.get(target):
            module.add_source(name)


for module in MODULES.values():
    print(module.__str__())


low_pulse_count = 0
high_pulse_count = 0
for _ in range(1000):
    SIGNALS = [(None, "broadcaster", False)]

    while SIGNALS:
        source, target, signal = SIGNALS.pop(0)
        if signal:
            high_pulse_count += 1
        else:
            low_pulse_count += 1
        if module := MODULES.get(target):
            module.receive(source, signal)
            for pulse in module.transmit():
                SIGNALS.append(pulse)

print(low_pulse_count * high_pulse_count)