T = [t.strip().split(" ") for t in open("aoc23/18.1.txt", 'r').readlines()]

y = 0
x = 0
P = []
for d, n, h in T:
    for i in range(int(n)):
        match (d):
            case "U":y -= 1
            case "D":y += 1
            case "R":x += 1
            case "L":x -= 1
        P.append((y, x))


miy = abs(min([y for y, _ in P]))
mix = abs(min([x for _, x in P]))

P = [(y + miy, x + mix) for y, x in P]

my = max([y for y, _ in P])
mx = max([x for _, x in P])

def is_l(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] < b[0] and b[0] == c[0] and b[1] < c[1]) or (c[0] < b[0] and b[0] == a[0] and b[1] < a[1])

def is_j(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] < b[0] and b[0] == c[0] and b[1] > c[1]) or (c[0] < b[0] and b[0] == a[0] and b[1] > a[1])

def is_7(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] == b[0] and b[0] < c[0] and a[1] < b[1]) or (c[0] == b[0] and b[0] < a[0] and c[1] < b[1])

def is_f(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] == b[0] and b[0] < c[0] and a[1] > b[1]) or (c[0] == b[0] and b[0] < a[0] and c[1] > b[1])

r = 0
R = []
for y in range(my+1):
    before = None
    is_in = False
    p_1 = None
    p_2 = None
    p_3 = None
    for x in range(mx+1):
        try:
            i = P.index((y, x))
        except ValueError:
            if is_in:
                R.append((y, x))
                r += 1
            continue
        y0, x0 = P[(i-1) % (len(P))]
        y1, x1 = P[(i+1) % (len(P))]
        if x0 == x == x1:
            is_in = not is_in
        elif y0 == y == y1:
            pass
        elif p_1 is None:
            p_1 = (y0, x0)
            p_2 = (y, x)
            p_3 = (y1, x1)
            before = is_in
            is_in = True
        elif (is_l(p_1, p_2, p_3) and is_7((y0, x0), (y, x), (y1, x1))) or (is_f(p_1, p_2, p_3) and is_j((y0, x0), (y, x), (y1, x1))):            
            is_in = not before
            before = None
            p_1 = None
            p_2 = None
        else:
            is_in = before
            before = None
            p_1 = None
            p_2 = None
        R.append((y, x))
        r += 1

print(r)
