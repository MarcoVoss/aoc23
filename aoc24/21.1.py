from abc import abstractmethod


class IKeypad:
    def get_key(self, key: str) -> tuple[int, int]:
        return self.get_keys().get(key)

    @abstractmethod
    def get_keys(self) -> dict[str, tuple[int, int]]:
        ...

    @abstractmethod
    def get_invalid_position(self) -> list[tuple[int, int]]:
        ...

    @abstractmethod
    def get_activate_position(self) -> tuple[int, int]:
        ...


class NumericKeypad(IKeypad):
    A = "A"

    def get_keys(self):
        return {
            '0': (3, 1),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            self.A: (3, 2),
        }

    def get_invalid_position(self):
        return (3, 0)

    def get_activate_position(self) -> tuple[int, int]:
        return (3, 2)


class DirectionalKeypad(IKeypad):
    A = "A"
    DOWN = "v"
    UP = "^"
    RIGHT = ">"
    LEFT = "<"

    def get_keys(self):
        return {
            self.DOWN: (1, 1),
            self.UP: (0, 1),
            self.RIGHT: (1, 2),
            self.LEFT: (1, 0),
            self.A: (0, 2),
        }

    def get_invalid_position(self):
        return (0, 0)

    def get_activate_position(self) -> tuple[int, int]:
        return (0, 2)


class Robot:
    def __init__(self, keypad: IKeypad, output: list[str]):
        self.keypad = keypad
        self.output = output
        self.active_position = keypad.get_activate_position()
        self.invalid_position = keypad.get_invalid_position()
        print("IN: ", self.output)

    def get_inputs(self):
        ly, lx = self.active_position
        input_combinations: list[list[str]] = []
        for key in self.output:
            iy, ix = self.invalid_position
            cy, cx = self.keypad.get_key(key)

            vy = cy - ly
            vx = cx - lx
            vs = "^" if vy < 0 else "v"
            hs = "<" if vx < 0 else ">"
            input_combinations.append([
                vs * (v - 1) + hs * (vx) + vs * (vy - v - 1) + "A"
                for v in range(1, vy + 1)
            ])
            ly, lx = cy, cx
        print("OU: ", input_combinations)
        return input_combinations


result = 0
for code in open('21.1.txt').readlines():
    code = list(code.strip())

    minimum_length = min([
        len(possible_input_1) + len(possible_input_2) + len(possible_input_3)
        for possible_input_1 in Robot(NumericKeypad(), code).get_inputs()
        for possible_input_2 in Robot(DirectionalKeypad(), possible_input_1).get_inputs()
        for possible_input_3 in Robot(DirectionalKeypad(), possible_input_2).get_inputs()
    ])

    numeric_part = int(code[:-1])
    result += numeric_part * minimum_length
print(result)
