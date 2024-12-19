MAP: list[list[str]] = []
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

for y, line in enumerate(open('16.1.txt').readlines()):
    MAP.append(list(line.strip()))
    COSTS.append([0] * len(line.strip()))

    try:
        START = y, line.index(START_SYMBOL)
    except ValueError:
        pass

    try:
        END = y, line.index(END_SYMBOL)
    except ValueError:
        pass

CONNECTION: dict[tuple[int, int], tuple[int, int] | None] = {START: START}
fields_to_check = [(START, EAST)]

while fields_to_check:
    CURRENT, CURRENT_DIRECTION = fields_to_check.pop(0)

    for DIRECTION in DIRECTIONS:
        NEXT = (CURRENT[0] + DIRECTION[0], CURRENT[1] + DIRECTION[1])

        if DIRECTION == CURRENT_DIRECTION:
            TURN_COST = 0
        elif DIRECTION[0] == -CURRENT_DIRECTION[0] and DIRECTION[1] == -CURRENT_DIRECTION[1]:
            TURN_COST = 2000
        else:
            TURN_COST = 1000

        PREDICTED_COST = COSTS[CURRENT[0]][CURRENT[1]] + STEP_WIDTH + TURN_COST
        NEXT_COST = COSTS[NEXT[0]][NEXT[1]]

        if MAP[NEXT[0]][NEXT[1]] != BORDER and (NEXT_COST == 0 or NEXT_COST > PREDICTED_COST):
            CONNECTION[NEXT] = CURRENT
            fields_to_check.append((NEXT, DIRECTION))
            COSTS[NEXT[0]][NEXT[1]] = PREDICTED_COST

PATH_BACK = []
CURRENT = END
while True:
    PATH_BACK.append(CURRENT)
    if CURRENT == START:
        break
    CURRENT = CONNECTION[CURRENT]

PATH_BACK.reverse()
COST = 0
DIR = EAST
for i in range(1, len(PATH_BACK)):
    COST += 1
    CURRENT_DIR = (PATH_BACK[i][0] - PATH_BACK[i - 1][0], PATH_BACK[i][1] - PATH_BACK[i - 1][1])
    if CURRENT_DIR != DIR:
        DIR = CURRENT_DIR
        COST += 1000

print(COST)