content = [list(line) for line in open("aoc23/3.2.txt", 'r').readlines()]

stars: dict[tuple, list[int]] = {}
places: dict[tuple, list[tuple]] = {}
for l_i, line in enumerate(content):
    for c_i, char in enumerate(line):
        if char == "*":
            for x in [1, 0, -1]:
                for y in [1, 0, -1]:
                    if x or y:
                        places.setdefault((l_i + x, c_i + y), []).append((l_i, c_i))
                        stars[(l_i, c_i)] = []

for l_i, line in enumerate(content):
    number = ""
    should_add_to = []
    for c_i, char in enumerate(line):
        if char.isnumeric():
            number += char
            if (l_i, c_i) in places:
                should_add_to += places[(l_i, c_i)]
        else:
            for should_add in set(should_add_to):
                stars[should_add].append(int(number))
            number = ""
            should_add_to = []

print(sum([
    values[0] * values[1]
    for _, values in stars.items()
    if len(values) == 2
]))
