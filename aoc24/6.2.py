
M: list[list[int]] = []

EMPTY = 0
OBSTACLE = 1
GUARD = 2

P: list[tuple[tuple[int, int], tuple[int, int]]] = []
C: tuple[int, int] = (None, None)
X: list[int] = [0, 1, 0, -1]
Y: list[int] = [-1, 0, 1, 0]
V: tuple[int, int] = (0, 0)  # y, x


def mark(f: str) -> int:
    return {".": EMPTY, "#": OBSTACLE, "^": GUARD}.get(f)


for y, line in enumerate(open('6.2.txt').readlines()):
    M.append([])
    for x, f in enumerate(line.strip()):
        M[y].append(mark(f))
        if M[y][x] == GUARD:
            C = (y, x)

S = (C[0], C[1])


def inside(c: tuple[int, int]) -> bool:
    y, x = c
    return 0 <= y < len(M) and 0 <= x < len(M[0])


def is_obstacle_ahead(c: tuple[int, int], v: tuple[int, int]) -> bool:
    c = step_forward(c, v)
    return inside(c) and is_obstacle(c)


def is_obstacle(c: tuple[int, int]) -> bool:
    return M[c[0]][c[1]] == OBSTACLE


def starting_position(c: tuple[int, int]) -> tuple[int, int]:
    return c == S


def turn_right(v: tuple[int, int]) -> tuple[int, int]:
    return ((v[0] + 1) % 4, (v[1] + 1) % 4)


def step_forward(c: tuple[int, int], v: tuple[int, int]) -> tuple[int, int]:
    return (c[0] + Y[v[0]], c[1] + X[v[1]])


while inside(C):
    P.append((C, V))
    if is_obstacle_ahead(C, V):
        V = turn_right(V)
    else:
        C = step_forward(C, V)


def is_loop(i: int, c: tuple[int, int], v: tuple[int, int], o: tuple[int, int]) -> bool:
    path = set(P[:i])
    while True:
        if (c, v) in path:
            return True
        path.add((c, v))
        step = step_forward(c, v)
        if inside(step):
            if is_obstacle(step) or step == o:
                v = turn_right(v)
            else:
                c = step
        else:
            return False


def is_in_past(i, c: tuple[int, int]) -> bool:
    return any(c == c_ for c_, _ in P[:i])


SOLUTION = set()
for i, (c, v) in enumerate(P[1:]):
    front = step_forward(c, v)
    right_v = turn_right(v)
    right = step_forward(c, right_v)
    if (
        inside(front)
        and not is_obstacle(front)
        and not starting_position(front)
        and not is_in_past(i, front)
        and is_loop(i, c, right_v, front)
    ):
        SOLUTION.add(front)

print(len(SOLUTION))
