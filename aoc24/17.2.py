class InvalidOutput(Exception):
    pass


class Solver:
    def __init__(self, a: int, b: int, c: int, p: list[int]):
        self.A = a
        self.B = b
        self.C = c
        self.P = p
        self.instruction_pointer = 0
        self.output = []

    def get_literal_operand(self, operand: int) -> int:
        return operand

    def get_combo_operand(self, operand: int) -> int:
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        raise ValueError(f"Invalid operand {operand}")

    def apply_opcode(self, opcode: int, operand: int):
        match opcode:
            case 0:
                self.A = int(self.A / 2**self.get_combo_operand(operand))
            case 1:
                self.B = self.B ^ self.get_literal_operand(operand)
            case 2:
                self.B = (self.get_combo_operand(operand) % 8) & 7
            case 3:
                if self.A != 0 and (next_instruction := self.get_literal_operand(operand)) != self.instruction_pointer:
                    self.instruction_pointer = next_instruction
                    return
            case 4:
                self.B = self.B ^ self.C
            case 5:
                self.output.append(self.get_combo_operand(operand) % 8)
                if self.P[:len(self.output)] != self.output:
                    raise InvalidOutput()
            case 6:
                self.B = int(self.A / 2**self.get_combo_operand(operand))
            case 7:
                self.C = int(self.A / 2**self.get_combo_operand(operand))
        self.instruction_pointer += 2

    def solve(self):
        while self.instruction_pointer < len(self.P):
            opcode = self.P[self.instruction_pointer]
            operand = self.P[self.instruction_pointer+1]
            self.apply_opcode(opcode, operand)
        return ",".join(map(str, self.output))


lines = open('17.2.txt').readlines()
b = int(lines[1].split(": ")[1].strip()),
c = int(lines[2].split(": ")[1].strip()),
p = list(map(int, list(lines[4].split(": ")[1].strip().split(","))))
a = 1
while True:
    solver = Solver(a, b, c, p)
    try:
        if solver.solve() == ",".join(map(str, solver.P)):
            break
    except InvalidOutput:
        pass
    a += 1

print("Result: ", a)
