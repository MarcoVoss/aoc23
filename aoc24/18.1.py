lines = open('18.1.txt').readlines()
WIDTH = 71
HEIGHT = 71
START = 0, 0
END = 70, 70
CORRUPTED = [tuple(reversed(list(map(int, line.strip().split(","))))) for line in lines][:1024]
COSTS: dict[tuple[int, int], int] = {START: 0}
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

TO_CHECK = [START]
while TO_CHECK:
    CURRENT = TO_CHECK.pop(0)
    NEXT_COSTS = COSTS[CURRENT] + 1
    for DIRECTION in DIRECTIONS:
        NEXT = CURRENT[0] + DIRECTION[0], CURRENT[1] + DIRECTION[1]
        if (
            NEXT not in CORRUPTED and
            0 <= NEXT[0] < HEIGHT and
            0 <= NEXT[1] < WIDTH and (
                NEXT not in COSTS or
                NEXT_COSTS < COSTS[NEXT]
            )
        ):
            COSTS[NEXT] = NEXT_COSTS
            TO_CHECK.append(NEXT)

print(COSTS[END])
