T = [t.strip().split(" ") for t in open("aoc23/18.2.txt", 'r').readlines()]

y = 0
x = 0
P = []
# for _, _, h in T:
#     n = int(h[2:-2], 16)
#     d = int(h[-2])
#     for i in range(int(n)):
#         match (d):
#             case 0:x += 1
#             case 1: y += 1
#             case 2:x -= 1
#             case 3: y -= 1
#         P.append((y, x))
for d, n, h in T:
    for i in range(int(n)):
        match (d):
            case "U":y -= 1
            case "D":y += 1
            case "R":x += 1
            case "L":x -= 1
        P.append((y, x))

def is_l(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] < b[0] and b[0] == c[0] and b[1] < c[1]) or (c[0] < b[0] and b[0] == a[0] and b[1] < a[1])

def is_j(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] < b[0] and b[0] == c[0] and b[1] > c[1]) or (c[0] < b[0] and b[0] == a[0] and b[1] > a[1])

def is_7(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] == b[0] and b[0] < c[0] and a[1] < b[1]) or (c[0] == b[0] and b[0] < a[0] and c[1] < b[1])

def is_f(a: tuple[int], b: tuple[int], c: tuple[int]) -> bool:
    return (a[0] == b[0] and b[0] < c[0] and a[1] > b[1]) or (c[0] == b[0] and b[0] < a[0] and c[1] > b[1])

def get_part(a: tuple[int], b: tuple[int], c: tuple[int]) -> None|str:
    if a[0] == b[0] == c[0]:
        return None
    if is_l(a, b, c):
        return "L"
    if is_j(a, b, c):
        return "J"
    if is_7(a, b, c):
        return "7"
    if is_f(a, b, c):
        return "F"
    if a[1] == b[1] == c[1]:
        return "|"

l_p = len(P) - 1
def get_p(i: int) -> tuple[int, int, int, int]:
    y0, x0 = P[-1 if i == 0 else i-1]
    y1, x1 = P[0 if i == l_p else i+1]
    return y0, x0, y1, x1

G: dict[int, list[tuple[int, int]]] = {}
for i, (y, x) in enumerate(P):
    y0, x0, y1, x1 = get_p(i)
    G.setdefault(y, []).append((x, get_part((y0, x0), (y, x), (y1, x1)))) 

R = []
r = 0
for y, E in G.items():
    r += len(E)
    before = None
    l_p = None
    l_x = None
    is_in = False
    for x, p in sorted(E, key=lambda k: k[0]):
        if p:
            if p == "|":
                if is_in and l_x is not None:
                    r += (x - l_x - 1) 
                is_in = not is_in
            elif l_p is None:
                if is_in and l_x is not None:
                    r += (x - l_x - 1) 
                l_p = p
                before = is_in
                is_in = True  
            elif (l_p == "L" and p == "7") or (l_p == "F" and p == "J"):         
                is_in = not before
                before = None
                l_p = None
            else:
                is_in = before
                before = None
                l_p = None
            l_x = x

# for i in range(my+1):
#     print("".join(["#" if (i, j) in P else "." for j in range(mx+1)]))

# print("==================")

print(r)
