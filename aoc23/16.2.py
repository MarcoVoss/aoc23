T = []

for i, t in enumerate(open("aoc23/16.2.txt", 'r').readlines()):
    _t = []
    for j, f in enumerate(t):
        top = (i-1, j)
        right = (i, j+1)
        bottom = (i+1, j)
        left = (i, j-1)
        match(f):
            case ".":
                _t.append({
                    top: (bottom,),
                    bottom: (top,),
                    left: (right,),
                    right: (left,)
                })
            case "|":
                _t.append({
                    top: (bottom,),
                    bottom: (top,),
                    left: (top, bottom),
                    right: (top, bottom),
                })
            case "-":
                _t.append({
                    top: (left, right),
                    bottom: (left, right),
                    left: (right,),
                    right: (left,)
                })
            case "\\":
                _t.append({
                    top: (right,),
                    bottom: (left,),
                    left: (bottom,),
                    right: (top,)
                })
            case "/":
                _t.append({
                    top: (left,),
                    bottom: (right,),
                    left: (top,),
                    right: (bottom,)
                })
    T.append(_t)



M = []
S = [((y, -1), (y, 0)) for y in range(len(T))]
S += [((y, len(T[y])), (y, len(T[y])-1)) for y in range(len(T))]
S += [((-1, x), (0, x)) for x in range(len(T[0]))]
S += [((len(T), x), (len(T)-1, x)) for x in range(len(T[0]))]

for s in S:
    V = []
    E = []
    places = [s]
    while places:
        p, c = places.pop()
        if (p, c) in V:
            continue
        V.append((p, c))
        E.append(c)
        for n in T[c[0]][c[1]][p]:
            if 0 <= n[0] < len(T) and 0 <= n[1] < len(T[0]):
                places.append((c, n))
    M.append(len(set(E)))
print(max(M))
