P = [list(line.strip()) for line in open("aoc23/23.2.txt", 'r').readlines()]

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
        if c != "#" and i != len(P)-1:
            r = [n for d in [UP, DOWN, LEFT, RIGHT] if (n := step((i, j), d))]
        else:
            r = []
        R.append(r)
    T.append(R)

a = (-1, 1)
s = (0, 1)
e = (y := len(T) - 1, len(T[y]) - 2)
V = {a: None}
S: list[tuple[tuple[int, int], tuple[int, int]]] = [(a, s)]

def get_path(p: tuple[int, int]) -> list[tuple[int, int]]:
    pre = []
    while p:
        pre.append(p)
        p = V[p]
    return pre


print("Build")
while S:
    p, c = S.pop()
    pre = get_path(p)

    if c not in V:
        print("T")
        for n in T[c[0]][c[1]]:
            if n not in pre:
                S.append((c, n))
        V[c] = p
    elif len(pre) > len(get_path(V[c])):
        print("S")
        while c != s:
            c_ = V[c]
            V[c] = p
            p = c
            c = c_
    else:
        print("E")
        while c != s:
            p_ = V[p]
            V[p] = c
            c = p
            p = p_

print(len(V))

print("Analyze")
r = 0
n = e
TEST = []
while n:
    r += 1
    TEST.append(n)
    n = V.get(n)

for i, p in enumerate(P):
    print("".join([c if (i, j) not in TEST else "O" for j, c in enumerate(p)]))

print(r)
