T = [["#" if p == "#" else 0 for p in l]for l in open("aoc23/11.2.txt", 'r').readlines()]
T = [t if "#" in t else [1000000 for _ in range(len(t))] for t in T]
T = [[g if "#" in [k[j] for k in T] else g + 1000000 for j, g in enumerate(t)] for t in T]
P = [(i, j) for i, t in enumerate(T) for j, g in enumerate(t) if g == "#"]
T = [[1 if g in ["#", 0] else g for g in t] for t in T]
S = [
    (
        sum(T[p[0]][x] for x in range(p[1], q[1], 1 if p[1] < q[1] else -1)) +
        sum(T[y][q[1]] for y in range(p[0], q[0], 1 if p[0] < q[0] else -1))          
    )
    for i, p in enumerate(P[:-1])
    for q in P[i+1:]
]

print(sum(S))
