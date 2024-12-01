seeds = [int(number) for number in open("aoc23/5.1.txt", 'r').readlines()[0].split(": ")[1].split(" ") if number]

content: list[list[int]] = []
for line in open("aoc23/5.1.txt", 'r').readlines()[1:]:
    if line.strip() == "":
        content.append([])
    elif line[0].isdigit():
        content[-1].append([int(number) for number in line.strip().split(" ") if number])

mapped_seeds = {}
for seed in seeds:
    current_value = seed
    for table in content:
        for c in table:
            if c[1] <= current_value < c[1] + c[2]:
                current_value = c[0] + current_value - c[1]
                break
    mapped_seeds[seed] = current_value

print(min(mapped_seeds.values()))
