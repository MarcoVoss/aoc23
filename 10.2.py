
T = [list(l.strip()) for l in open("aoc23/10.2.txt", 'r').readlines()]

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
    (i + direction[0], t + direction[1])
    for direction in directions.get(T[i][t])
]

loop = []
for way in ways:
    if not is_connected(i, t, *way):
        continue

    points = [(i, t), way]

    p = None
    c = way
    while not loop:
        f = T[c[0]][c[1]]

        if f == "S" and len(points) > 3:
            loop = points
            break

        connected = [
            (c1, c2)
            for d in directions.get(f)
            if is_connected(*c, (c1 := c[0] + d[0]), (c2 := c[1] + d[1])) and (c1, c2) != p
        ]

        if not connected:
            break
        
        p = c
        c = connected[0]
        points.append(c)

    if loop:
        break

T[i][t] = {
    -1: {
        -1: "J",
        0: "|",
        1: "7",
    },
    0: {
        -1: "-",
        1: "-",
    },
    1: {
        -1: "F",
        0: "|",
        1: "L",
    }

}.get(loop[1][0] - loop[-1][0]).get(loop[1][1] - loop[-1][1])


INSIDE = 0
OUTSIDE = 1
ON_TOP = 2

selected = []
fields = []
states = []
for i, t in enumerate(T):
    state_before = OUTSIDE
    state = OUTSIDE
    top_field = None
    for j, p in enumerate(t[:-1]):
        if i == 107:
            fields.append(p if (i, j) in loop else ".")
            states.append(str(state))
        if (i, j) in loop:
            match T[i][j]:
                case "L" | "F":
                    state_before = state
                    state = ON_TOP
                    top_field = T[i][j]
                case "J" | "7":
                    if (top_field, T[i][j]) in [("L", "7"), ("F", "J")]:
                        state = OUTSIDE if state_before == INSIDE else INSIDE
                    else:
                        state = state_before
                    top_field = None
                case "|":
                    state = OUTSIDE if state == INSIDE else INSIDE
        elif state == INSIDE:
                selected.append((i, j))

for i, t in enumerate(T):
    print(
        "".join([p if (i, j) in loop else ("#" if (i, j) in selected else ".")
        for j, p in enumerate(t)])
    )

print("".join(fields))
print("".join(states))

# print(selected)
print(len(set(selected)))
