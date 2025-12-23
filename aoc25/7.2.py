lines = list(map(list, open("7.2.txt", 'r').readlines()))

START = lines[0].index("S")

positions = {START: 1}

for y in range(len(lines)):
    new_positions = {}
    for x, count in positions.items():
        if lines[y][x] == "^":
            new_positions.setdefault(x-1, 0)
            new_positions[x-1] += count
            new_positions.setdefault(x+1, 0)
            new_positions[x+1] += count
        else:
            new_positions.setdefault(x, 0)
            new_positions[x] += count

    positions = new_positions

print(sum(positions.values()))
