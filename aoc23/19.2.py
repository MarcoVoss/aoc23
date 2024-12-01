
T = [t.strip() for t in open("aoc23/19.2.txt", 'r').readlines()]

i = 0
W: dict[str, list] = {}
while T[i] != "":
    t = T[i]
    name, workflow = t.split("{")
    workflow = workflow[:-1].split(",")
    workflow = [w.split(":") if ":" in w else w for w in workflow]
    W[name] = workflow
    i += 1

def copy_dict(d: dict) -> dict:
    import copy
    return copy.deepcopy(d)

A: list[dict] = []
R: list[dict] = [{
    "x": [1, 4000],
    "m": [1, 4000],
    "a": [1, 4000],
    "s": [1, 4000],
    "t": "in",
}]
while R:
    a = R.pop()
    if a["t"] == "A":
        A.append(a)
    elif a["t"] != "R":
        w = W[a["t"]]
        g = copy_dict(a)
        g["t"] = w[-1]
        for e in w[:-1]:
            e, t = e[0], e[1]
            b = copy_dict(g)
            b["t"] = t
            v = int(e[2:])
            if e[1] == "<":
                b[e[0]][1] = min(b[e[0]][1], v-1)
                g[e[0]][0] = max(g[e[0]][0], v)
            else:
                b[e[0]][0] = max(b[e[0]][0], v+1)
                g[e[0]][1] = min(g[e[0]][1], v)
            R.append(b)
        R.append(g)


THE_MAX = 0

for i in range(len(A)):
    max_x = A[i]["x"][1]
    min_x = A[i]["x"][0]
    x = max_x - min_x + 1

    max_m = A[i]["m"][1]
    min_m = A[i]["m"][0]
    m = max_m - min_m + 1

    max_a = A[i]["a"][1]
    min_a = A[i]["a"][0]
    a = max_a - min_a + 1

    max_s = A[i]["s"][1]
    min_s = A[i]["s"][0]
    s = max_s - min_s + 1

    THE_MAX += (x * m * a * s)

for i in range(len(A)):
    for j in range(i+1, len(A)):
        max_x = min(A[i]["x"][1], A[j]["x"][1])
        min_x = max(A[i]["x"][0], A[j]["x"][0])
        x = max_x - min_x if max_x > min_x else 0

        max_m = min(A[i]["m"][1], A[j]["m"][1])
        min_m = max(A[i]["m"][0], A[j]["m"][0])
        m = max_m - min_m if max_m > min_m else 0

        max_a = min(A[i]["a"][1], A[j]["a"][1])
        min_a = max(A[i]["a"][0], A[j]["a"][0])
        a = max_a - min_a if max_a > min_a else 0

        max_s = min(A[i]["s"][1], A[j]["s"][1])
        min_s = max(A[i]["s"][0], A[j]["s"][0])
        s = max_s - min_x if max_s > min_s else 0
        THE_MAX -= (x * m * a * s)

print(THE_MAX)