COSTS: list[list[int]] = []
START: tuple[int, int] = (0, 0)
END: tuple[int, int] = (0, 0)
STEP_WIDTH = 1
EAST = (0, STEP_WIDTH)
SOUTH = (STEP_WIDTH, 0)
WEST = (0, -STEP_WIDTH)
NORTH = (-STEP_WIDTH, 0)
DIRECTIONS: list[tuple[int, int]] = [EAST, SOUTH, WEST, NORTH]
BORDER = "#"
START_SYMBOL = "S"
END_SYMBOL = "E"
INFINITE = -1
INITIAL = -2

for y, line in enumerate(open('16.2.txt').readlines()):
    costs = []
    for x, place in enumerate(line.strip()):
        if place == BORDER:
            costs.append(INFINITE)
        else:
            costs.append(INITIAL)
            if place == START_SYMBOL:
                START = y, x
            elif place == END_SYMBOL:
                END = y, x
    COSTS.append(costs)

COSTS[START[0]][START[1]] = 0
to_check = [(START, EAST)]
while to_check:
    (cy, cx), (cdy, cdx) = to_check.pop(0)
    cc = COSTS[cy][cx]
    for dy, dx in DIRECTIONS:
        ny, nx = cy + dy, cx + dx

        if 0 <= ny < len(COSTS) and 0 <= nx < len(COSTS[0]) and COSTS[ny][nx] != INFINITE:
            pc = cc + 1
            if (dy, dx) == (cdy, cdx):
                pc += 0
            elif dy == -cdy and dx == -cdx:
                pc += 2000
            else:
                pc += 1000
            if COSTS[ny][nx] == INITIAL or COSTS[ny][nx] >= pc:
                to_check.insert(0, ((ny, nx), (dy, dx)))
                COSTS[ny][nx] = pc

TO_CHECK = [(END, None)]
PATH_BACK = set()
while TO_CHECK:
    # have to check the direction too, for the statements in line 60 and 62
    (cy, cx), direction = TO_CHECK.pop(0)
    PATH_BACK.add((cy, cx))
    cc = COSTS[cy][cx]

    for dy, dx in DIRECTIONS:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < len(COSTS) and 0 <= nx < len(COSTS[0]) and COSTS[ny][nx] != INFINITE:
            if (cy, cx) == END:
                if COSTS[ny][nx] == cc - 1:
                    TO_CHECK.append(((ny, nx), (dy, dx)))
            elif direction == (dy, dx):
                if COSTS[ny][nx] in [cc - 1, cc - 1000 - 1, cc + 1000 - 1]:
                    TO_CHECK.append(((ny, nx), (dy, dx)))
            elif COSTS[ny][nx] in [cc - 1, cc - 1000 - 1]:
                TO_CHECK.append(((ny, nx), (dy, dx)))

for y, line in enumerate(COSTS):
    l = ""
    for x, cost in enumerate(line):
        if cost == INFINITE:
            l += "      "
        else:
            l += " " + str(COSTS[y][x]).zfill(5)
    print(l)

print(len(PATH_BACK))

# 499 too high
