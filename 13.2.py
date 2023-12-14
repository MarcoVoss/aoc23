T = [[]]
for l in open("aoc23/13.2.txt", 'r').readlines():
    l = l.strip()
    if not l:
        T.append([])
    else:
        T[-1].append(l)


def turn(t: list[str]) -> list[str]:
    R = []
    for i in range(len(t[0])):
        r = ""
        for j in range(len(t)):
            r += t[j][i]
        R.append(r)
    return R


def dif(a: list[str], b: list[str]) -> int:
    return len([1 for i in range(len(a)) if a[i] != b[i] for j in range(len(a[i])) if a[i][j] != b[i][j]])


def check(a: list[str], b: list[str]) -> int:
    return dif(a, b[::-1])


def solve(t: list[str]) -> int:
    E = [i + 1 for i, (a, b) in enumerate(zip(t[:-1], t[1:])) if dif(a, b) < 2]
    G = []
    for e in E:
        if 2 * (e) < len(t):
            d = check(t[:e], t[e: 2 * (e)])
            if d == 1:
                G.append(e)
        elif e - (len(t) - e) >= 0:
            d = check(t[e - (len(t) - e):e], t[e:])
            if d == 1:
                G.append(e)
    print(G)
    return sorted(G, key=lambda x: len(t) - x)[-1] if G else 0

result = 0
for i, t in enumerate(T):
    print("->", i)
    h = solve(t)
    v = solve(turn(t))
    if v > h:
        result += (v)
    else:
        result += (h) * 100
print(result)
