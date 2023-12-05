seeds = [int(number) for number in open("aoc23/5.2.txt", 'r').readlines()[0].split(": ")[1].split(" ") if number]

content: list[list[int]] = []
for line in open("aoc23/5.2.txt", 'r').readlines()[1:]:
    if line.strip() == "":
        content.append([])
    elif line[0].isdigit():
        content[-1].append([int(number) for number in line.strip().split(" ") if number])

mapped_seeds = {}
starting_points = seeds[::2]
ranges = seeds[1::2]

min_value = -1
result = None
while result is None:
    min_value += 1
    current_value = min_value
    for table in content[::-1]:
        for c in table:
            if c[0] <= current_value < c[0] + c[2]:
                current_value = current_value - c[0] + c[1]
                break
    for index, seed in enumerate(starting_points):
        if seed <= current_value < seed + ranges[index]:
            result = current_value
            break

print(min_value)
