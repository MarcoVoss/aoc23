content = [list(line) for line in open("aoc23/3.1.txt", 'r').readlines()]

places = [
    (l_i + x, c_i + y)
    for l_i, line in enumerate(content)
    for c_i, char in enumerate(line)
    if not char.isnumeric() and char not in [".", "\n"]
    for x in [1, 0, -1]
    for y in [1, 0, -1]
    if x or y
]

result = 0
for l_i, line in enumerate(content):
    number = ""
    should_add = False
    for c_i, char in enumerate(line):
        if char.isnumeric():
            number += char
            if (l_i, c_i) in places:
                should_add = True
        else:
            if should_add:
                result += int(number)
            number = ""
            should_add = False

print(result)
