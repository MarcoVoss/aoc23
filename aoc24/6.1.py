
M: list[list[int]] = []

EMPTY = 0
OBSTACLE = 1
GUARD = 2

P = set()
C: tuple[int, int] = (None, None)
X: list[int] = [0, 1, 0, -1]
Y: list[int] = [-1, 0, 1, 0]
V: tuple[int, int] = (0, 0)  # y, x


def mark(f: str) -> int:
    return {".": EMPTY, "#": OBSTACLE, "^": GUARD}.get(f)


for y, line in enumerate(open('6.1.txt').readlines()):
    M.append([])
    for x, f in enumerate(line.strip()):
        M[y].append(mark(f))
        if M[y][x] == GUARD:
            C = (y, x)


def inside(c: tuple[int, int]) -> bool:
    y, x = c
    return 0 <= y < len(M) and 0 <= x < len(M[0])


def obstacle_ahead(c: tuple[int, int]) -> bool:
    y, x = step_forward(c)
    return inside((y, x)) and M[y][x] == OBSTACLE


def step_forward(c: tuple[int, int]) -> tuple[int, int]:
    return (c[0] + Y[V[0]], c[1] + X[V[1]])


def turn_right(v: tuple[int, int]) -> tuple[int, int]:
    return ((v[0] + 1) % 4, (v[1] + 1) % 4)


while inside(C):
    if obstacle_ahead(C):
        V = turn_right(V)
    else:
        P.add(C)
        C = step_forward(C)

print(len(P))
