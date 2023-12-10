
T = [list(l) for l in open("aoc23/10.1.txt", 'r').readlines()]

# (y, x)
TOP = (-1, 0)
RIGHT = (0, 1)
BOTTOM = (1, 0)
LEFT = (0, -1)

directions = {
    "|": (TOP, BOTTOM),
    "-": (LEFT, RIGHT),
    "L": (TOP, RIGHT),
    "J": (TOP, LEFT),
    "7": (LEFT, BOTTOM),
    "F": (BOTTOM, RIGHT),
    ".": (),
    "S": (TOP, RIGHT, BOTTOM, LEFT),
}

def find_start():
    for i, t in enumerate(T):
        try:
            return (i, t.index("S"))
        except ValueError:
            pass


def is_connected(i0: int, t0: int, i1: int, t1: int) -> bool:
    return (
        0 <= i1 < len(T)
        and 0 <= t1 < len(T[i1])
        and any((i0, t0) == ((i := i1 + direction[0]), (t := t1 + direction[1]))
        for direction in directions.get(T[i1][t1])
    ))


def find_next(i0: int, t0: int, i1: int, t1: int) -> tuple[int, int]:
    return [
        (i, t)
        for direction in directions.get(T[i1][t1])
        if (i0, t0) != ((i := i1 + direction[0]), (t := t1 + direction[1]))
    ][0]

i, t = find_start()

ways = [
    ((i, t), (i + direction[0], t + direction[1]))
    for direction in directions.get(T[i][t])
]

i = 0
while ways:
    ways = [
        (curr, (new))
        for (prev, curr) in ways
        if (
            T[curr[0]][curr[1]] not in [".", "S"]
            and (new := find_next(*prev, *curr))
        )
    ]

    i += 1

print(i // 2)
