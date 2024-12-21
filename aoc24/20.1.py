lines = open('20.1.txt').readlines()

START = 0, 0
END = 0, 0
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
BORDER = -1
INITIAL = -2

COSTS: list[list[int]] = []

# read
for y, line in enumerate(lines):
    row = []
    for x, char in enumerate(line.strip()):
        if char == "#":
            row.append(BORDER)
        else:
            if char == "S":
                START = y, x
                row.append(0)
            elif char == "E":
                END = y, x
                row.append(INITIAL)
            else:
                row.append(INITIAL)

    COSTS.append(row)


# calculate
to_check = [START]
while to_check:
    cy, cx = to_check.pop(0)
    cc = COSTS[cy][cx]

    for dy, dx in DIRECTIONS:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < len(COSTS) and 0 <= nx < len(COSTS[0]) and COSTS[ny][nx] != BORDER:
            pc = cc + 1
            if COSTS[ny][nx] == INITIAL or COSTS[ny][nx] > pc:
                to_check.insert(0, (ny, nx))
                COSTS[ny][nx] = pc

# collect
PATH = []
VERTICAL: dict[int, list[tuple[int, int]]] = {}
HORIZONTAL: dict[int, list[tuple[int, int]]] = {}
current = END
while True:
    PATH.append(current)
    VERTICAL.setdefault(current[0], []).append(current)
    HORIZONTAL.setdefault(current[1], []).append(current)
    if current == START:
        break

    cc = COSTS[current[0]][current[1]]
    for dy, dx in DIRECTIONS:
        nc = COSTS[current[0] + dy][current[1] + dx]
        if nc != BORDER and nc < cc:
            current = current[0] + dy, current[1] + dx
            break

# analyze
CHECK: list[tuple[tuple[int, int], tuple[int, int]]] = []
for line in VERTICAL.values():
    line = sorted(line, key=lambda x: x[1])
    for i in range(1, len(line)):
        if abs(line[i][1] - line[i-1][1]) == 2:
            CHECK.append((line[i-1], line[i]))

for line in HORIZONTAL.values():
    line = sorted(line, key=lambda x: x[0])
    for i in range(1, len(line)):
        if abs(line[i][0] - line[i-1][0]) == 2:
            CHECK.append((line[i-1], line[i]))

result = 0
for s, e in CHECK:
    diff = abs(PATH.index(s) - PATH.index(e)) - 2
    if diff >= 100:
        result += 1

print(result)
