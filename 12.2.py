T = [l.strip().split(" ") for l in open("aoc23/12.2.txt", 'r').readlines()]
n = 1
S = [("?".join([s for _ in range(n)]), [int(i) for _ in range(n) for i in k.split(",")],) for s, k in T]

R = []
for text, numbers in S:
    P = []
    ma = 0
    mi = 0
    for i, c in enumerate(text):
        match (c):
            case ".":
                if ma or mi:
                    P.append((mi, ma))
                    mi = 0
                    ma = 0
            case "#":
                mi += 1
                ma += 1
            case "?":
                ma += 1
    if ma or mi:
        P.append((mi, ma))
    R.append(P)
for r in R:
    print(r)