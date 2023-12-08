instructions = [0 if x == "L" else 1 for x in open("aoc23/8.1.txt", 'r').readlines()[0].strip()]

mapping = {}
for x in open("aoc23/8.1.txt", 'r').readlines()[2:]:
    splitted = x.strip().split(" = ")
    mapping[splitted[0]] = splitted[1][1:-1].split(", ")

index = 0
current = "AAA"
while current != "ZZZ":
    current = mapping[current][instructions[index % len(instructions)]]
    index += 1

print(index)
