lines = open('15.2.txt').readlines()
MAP: list[list[str]] = []
MOVES: list[str] = []
START = (0, 0)
y = -1
while lines:
    y += 1
    line = lines.pop(0).strip()
    if line == "":
        break
    line = line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    MAP.append(list(line))
    try:
        START = y, line.index("@")
    except ValueError:
        continue

for line in lines:
    MOVES.extend(list(line.strip()))

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

for move in MOVES:
    if move == "<":
        DIRECTION = LEFT
    elif move == "^":
        DIRECTION = UP
    elif move == ">":
        DIRECTION = RIGHT
    elif move == "v":
        DIRECTION = DOWN

    MOVING: list[set[tuple[int, int]]] = [[START]]
    TO_MOVE: list[set[int, int]] = [START]
    SHOULD_MOVE = True
    while True:
        if DIRECTION in [UP, DOWN]:
            NEXT_LINE = set()
            for place in MOVING[-1]:
                NEXT = (place[0] + DIRECTION[0], place[1] + DIRECTION[1])
                if MAP[NEXT[0]][NEXT[1]] == ".":
                    continue
                NEXT_LINE.add(NEXT)
                if MAP[NEXT[0]][NEXT[1]] == "[":
                    NEXT_LINE.add((NEXT[0], NEXT[1] + 1))
                elif MAP[NEXT[0]][NEXT[1]] == "]":
                    NEXT_LINE.add((NEXT[0], NEXT[1] - 1))
                elif MAP[NEXT[0]][NEXT[1]] == "#":
                    SHOULD_MOVE = False
                    break
            if not SHOULD_MOVE:
                break
            elif all(MAP[p[0]][p[1]] == "." for p in NEXT_LINE):
                break
            else:
                MOVING.append(NEXT_LINE)
        else:
            END = START
            while True:
                END = (END[0] + DIRECTION[0], END[1] + DIRECTION[1])
                if MAP[END[0]][END[1]] == "#":
                    SHOULD_MOVE = False
                    break
                elif MAP[END[0]][END[1]] == ".":
                    break
                else:
                    MOVING.append({END})
            break
    if SHOULD_MOVE:
        for line in reversed(MOVING):
            for place in line:
                NEXT = (place[0] + DIRECTION[0], place[1] + DIRECTION[1])
                MAP[place[0]][place[1]], MAP[NEXT[0]][NEXT[1]] = MAP[NEXT[0]][NEXT[1]], MAP[place[0]][place[1]]

        START = (START[0] + DIRECTION[0], START[1] + DIRECTION[1])

cost = 0
for y, row in enumerate(MAP):
    for x, place in enumerate(row):
        if place == "[":
            cost += 100 * y + x

print(cost)
