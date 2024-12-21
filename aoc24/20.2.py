lines = open('20.2.txt').readlines()

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
                row.append(INITIAL)
            elif char == "E":
                END = y, x
                row.append(0)
            else:
                row.append(INITIAL)

    COSTS.append(row)


# calculate
to_check = [END]
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


# for y, line in enumerate(COSTS):
#     l = ""
#     for x, cost in enumerate(line):
#         if cost == BORDER:
#             l += "   "
#         else:
#             l += " " + str(COSTS[y][x]).zfill(2)
#     print(l)

# collect
PATH: list[tuple[int, int]] = []
current = START
while True:
    PATH.append(current)
    if current == END:
        break

    cc = COSTS[current[0]][current[1]]
    for dy, dx in DIRECTIONS:
        nc = COSTS[current[0] + dy][current[1] + dx]
        if nc != BORDER and nc < cc:
            current = current[0] + dy, current[1] + dx
            break


def find_connected_paths(start: tuple[int, int], debug: dict[int, set[tuple[int, int]]]):
    sy, sx = start
    sc = COSTS[sy][sx]

    for oo in (1, -1):
        for y in range(21):
            dy = sy + y * oo
            if 0 <= dy < len(COSTS):
                for io in (1, -1):
                    for x in range(21 - y):
                        dx = sx + x * io
                        if 0 <= dx < len(COSTS[0]) and COSTS[dy][dx] != BORDER:
                            if COSTS[dy][dx] < sc - (y + x):
                                d = sc - (y + x) - COSTS[dy][dx]
                                debug.setdefault(d, set())
                                debug[d].add(((sy, sx), (dy, dx)))


debug = {}
result = 0
for path in PATH:
    i = PATH.index(path)
    find_connected_paths(path, debug)


for d, v in sorted(debug.items(), key=lambda x: x[0]):
    if d >= 100:
        result += len(v)
        # print(f"{d} -> {len(v)}")

print(result)
# not correct 9249
# too high 2077337
# too high 2372124
# too high 2401319
