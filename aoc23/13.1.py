T = [[]]
for l in open("aoc23/13.1.txt", 'r').readlines():
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


def solve(t: list[str]) -> int:
    E = [i + 1 for i, (a, b) in enumerate(zip(t[:-1], t[1:])) if a == b]
    G = []
    for e in E:
        if (
            (2 * (e) < len(t) and t[:e] == t[e: 2 * (e)][::-1]) or 
            (e - (len(t) - e) >= 0 and t[e - (len(t) - e):e][::-1] == t[e:])
        ):
            G.append(e)
    return sorted(G, key=lambda x: len(t) - x)[-1] if G else 0

result = 0
for t in T:
    h = solve(t)
    v = solve(turn(t))
    if v > h:
        result += (v)
    else:
        result += (h) * 100
print(result)