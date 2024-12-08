
M: dict[str, list[tuple[int, int]]] = {}

lines = open('8.1.txt').readlines()
for y, line in enumerate(lines):
    line = line.strip()
    for x, char in enumerate(line):
        if char != ".":
            M.setdefault(char, []).append((y, x))

Y_LIMIT = len(lines)
X_LIMIT = len(lines[0].strip())
R: set[tuple[int, int]] = set()

for points in M.values():
    for current in points:
        for other in points:
            if current == other:
                continue
            dy = other[0] - current[0]
            dx = other[1] - current[1]
            antinode_1 = other[0] + dy, other[1] + dx
            antinode_2 = current[0] - dy, current[1] - dx
            if 0 <= antinode_1[0] < Y_LIMIT and 0 <= antinode_1[1] < X_LIMIT:
                R.add(antinode_1)
            if 0 <= antinode_2[0] < X_LIMIT and 0 <= antinode_2[1] < X_LIMIT:
                R.add(antinode_2)

print(len(R))
