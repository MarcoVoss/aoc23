lines = open('15.1.txt').readlines()

MAP: list[list[str]] = []
MOVES: list[str] = []
START = (0, 0)
y = -1
while lines:
    y += 1
    line = lines.pop(0).strip()
    if line == "":
        break
    MAP.append(list(line))
    try:
        START = y, line.index("@")
    except ValueError:
        continue

for line in lines:
    MOVES.extend(list(line.strip()))

for move in MOVES:
    if move == "<":
        DIRECTION = (0, -1)
    elif move == "^":
        DIRECTION = (-1, 0)
    elif move == ">":
        DIRECTION = (0, 1)
    elif move == "v":
        DIRECTION = (1, 0)

    END = (START[0] + DIRECTION[0], START[1] + DIRECTION[1])

    while MAP[END[0]][END[1]] not in [".", "#"]:
        END = (END[0] + DIRECTION[0], END[1] + DIRECTION[1])

    if MAP[END[0]][END[1]] == ".":
        while END != START:
            PREVIOUS = (END[0] - DIRECTION[0], END[1] - DIRECTION[1])
            MAP[END[0]][END[1]], MAP[PREVIOUS[0]][PREVIOUS[1]] = MAP[PREVIOUS[0]][PREVIOUS[1]], MAP[END[0]][END[1]]
            END = PREVIOUS
        START = (START[0] + DIRECTION[0], START[1] + DIRECTION[1])

cost = 0
for y, row in enumerate(MAP):
    for x, place in enumerate(row):
        if place == "O":
            cost += 100 * y + x

print(cost)
