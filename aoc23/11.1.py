T = [list(l.strip()) for l in open("aoc23/11.1.txt", 'r').readlines()]
T = [t for t in T for _ in range(1 if "#" in t else 2)]
T = [[g for j, g in enumerate(t) for _ in range(1 if "#" in [k[j] for k in T] else 2)] for t in T]
P = [(i, j) for i, t in enumerate(T) for j, g in enumerate(t) if g == "#"]
S = [abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1]) for i in range(len(P)) for j in range(i + 1, len(P))]

print(sum(S))
