T = []

for i, t in enumerate(open("aoc23/16.1.txt", 'r').readlines()):
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



V = []
E = []
places = [((0, -1), (0, 0))]
while places:
    p, c = places.pop()
    if (p, c) in V:
        continue
    V.append((p, c))
    E.append(c)
    for n in T[c[0]][c[1]][p]:
        if 0 <= n[0] < len(T) and 0 <= n[1] < len(T[0]):
            places.append((c, n))

print(len(set(E)))