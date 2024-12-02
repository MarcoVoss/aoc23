P = [list(line.strip()) for line in open("aoc23/23.1.txt", 'r').readlines()]

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def step(b: tuple[int, int], d: tuple[int, int]) -> tuple[int, int] | None:
    yd = b[0] + d[0]
    xd = b[1] + d[1]
    return None if not 0 <= yd < len(P) or not 0 <= xd < len(P[yd]) or P[yd][xd] == "#" else (yd, xd)

T: list[list[list[tuple[int, int]]]] = []
for i, p in enumerate(P):
    R = []
    for j, c in enumerate(p):
        r = []
        match c:
            case "#":
                pass
            case ".":
                r +=  [n for d in [UP, DOWN, LEFT, RIGHT] if (n := step((i, j), d))]
            case "<":
                r += [n] if(n := step((i, j), LEFT)) else []
            case ">":
                r += [n] if(n := step((i, j), RIGHT)) else []
            case "v":
                r += [n] if(n := step((i, j), DOWN)) else []
            case "^":
                r += [n] if(n := step((i, j), UP)) else []
        R.append(r)
    T.append(R)

for t in T:
    print(t)

e = (y := len(T) - 1, len(T[y]) - 2)
F = []
W: list[list[tuple[int, int]]] = [[(-1, 1), (0, 1)]]
while W:
    steps = W.pop()
    y, x = steps[-1]
    for s in T[y][x]:
        if s not in steps:
            new = steps.copy() + [s]
            if s == e:
                F.append(new)
            else:
                W.append(new)

print(max(len(f[2:]) for f in F))
