
T = [list(l) for l in open("aoc23/10.1.txt", 'r').readlines()]

TOP = (-1, 0)
RIGHT = (0, 1)
BOTTOM = (1, 0)
LEFT = (0, -1)
NO = (0, 0)

directions = {
    "|": (TOP, BOTTOM),
    "-": (LEFT, RIGHT),
    "L": (TOP, RIGHT),
    "J": (TOP, LEFT),
    "7": (LEFT, BOTTOM),
    "F": (BOTTOM, RIGHT),
    ".": (NO, NO),
    "S": (TOP, RIGHT, BOTTOM, LEFT),
}

D = [
    [
        (
            (i + d[0][0], j + d[0][1]),
            (i + d[1][0], j + d[1][1]),
        )
        for j, p in enumerate(t)
        if (d := directions.get(p))
    ]
    for i, t in enumerate(T)
]

for k, t in enumerate(T):
    try:
        i, j = k, t.index("S")
        break
    except ValueError:
        pass


for d in D[i][j]:
    p = (i, j)
    c = d
    loop = [p]
    while c != (i, j):
        loop.append(c)

        (a, b) = D[c[0]][c[1]]

        if (a, b) == (NO, NO):
            break

        p, c = c, (a if a != p else b)
    else:
        break

print(len(loop) // 2)
