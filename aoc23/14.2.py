T: list[list[str]] = [list(l.strip()) for l in open("aoc23/14.2.txt", 'r').readlines()]

T = [[T[j][i] for j in range(len(T))] for i in range(len(T[0])-1,-1,-1)]

def calculate() -> int:
    return sum([
        len(t) - i
        for t in T
        for i in range(len(t))
        if t[i] == "O"
    ])

def make_hash():
    return hash("".join([x for t in T for x in t]))

P = {make_hash(): 0}
M = 1000000000
m = M
n = 0
while n < m:
    for _ in range(4):
        for k in range(len(T)):
            j = 0
            for i in range(len(T[k])):
                if T[k][i] == "#":
                    j = i + 1
                elif T[k][i] == "O":
                    T[k][i] = "."
                    T[k][j] = "O"
                    j += 1
        T = [list(t) for t in list(zip(*T[::-1]))]
    h = make_hash()
    if m != M:
        n += 1
    elif h in P:
        m = n + ((m - n) % (n - P.get(h)))
        n += 1
    else:
        P[h] = n
        n += 1

print(calculate())
