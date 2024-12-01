T = [t.strip() for t in open("aoc23/19.1.txt", 'r').readlines()]

i = 0
W = {}
while T[i] != "":
    t = T[i]
    name, workflow = t.split("{")
    workflow = workflow[:-1].split(",")
    workflow = [w.split(":") if ":" in w else w for w in workflow]
    W[name] = workflow
    i += 1

P = []
i += 1
while i < len(T):
    (x_r, m_r, a_r, s_r)  = T[i][1:-1].split(",")
    P.append({
        "x": int(x_r[2:]),
        "m": int(m_r[2:]),
        "a": int(a_r[2:]),
        "s": int(s_r[2:]),
    })
    i += 1


R: list[dict] = []
for p in P:
    n_w = "in"
    while n_w not in ["A", "R"]:
        w = W[n_w]
        for r in w:
            if type(r) is not list:
                n_w = r
                break
            else:
                r, t = r[0], r[1]
                c_r = p[r[0]]
                r_r = int(r[2:])
                if r[1] == "<" and c_r < r_r or r[1] == ">" and c_r > r_r:
                    n_w = t
                    break

    if n_w == "A":
        R.append(p)

print(sum([sum([v for v in r.values()]) for r in R]))