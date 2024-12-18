lines = open('18.2.txt').readlines()
WIDTH = 71
HEIGHT = 71
START = 0, 0
END = 70, 70
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
CORRUPTED = [tuple(reversed(list(map(int, line.strip().split(","))))) for line in lines]

for i in range(len(CORRUPTED), 1, -1):
    INNER_CORRUPTED = CORRUPTED[:i]
    COSTS: dict[tuple[int, int], int] = {START: 0}
    TO_CHECK = [START]
    while TO_CHECK:
        CURRENT = TO_CHECK.pop(0)
        NEXT_COSTS = COSTS[CURRENT] + 1
        for DIRECTION in DIRECTIONS:
            NEXT = CURRENT[0] + DIRECTION[0], CURRENT[1] + DIRECTION[1]
            if (
                NEXT not in INNER_CORRUPTED and
                0 <= NEXT[0] < HEIGHT and
                0 <= NEXT[1] < WIDTH and (
                    NEXT not in COSTS or
                    NEXT_COSTS < COSTS[NEXT]
                )
            ):
                COSTS[NEXT] = NEXT_COSTS
                TO_CHECK.append(NEXT)
    if END in COSTS:
        print(f"{CORRUPTED[i][1]},{CORRUPTED[i][0]}")
        break
