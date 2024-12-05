M: dict[int, tuple[set[int], set[int]]] = {}
U: list[list[int]] = []

lines = open('5.1.txt').readlines()
i = 0
while i < len(lines):
    row = lines[i].strip()
    i += 1
    if row == "":
        break
    l, r = row.strip().split("|")
    M.setdefault(int(l), (set(), set()))[1].add(int(r))
    M.setdefault(int(r), (set(), set()))[0].add(int(l))

while i < len(lines):
    U.append(list(map(int, lines[i].strip().split(","))))
    i += 1


def is_broken_page(u, i) -> bool:
    CL, CR = set(u[:i]), set(u[i+1:])
    L, R = M[u[i]]
    return (CL and not CL.issubset(L)) or (CR and not CR.issubset(R))


def is_broken_protocol(u) -> bool:
    return any(is_broken_page(u, i) for i, _ in enumerate(u))


result = 0
for u in U:
    if not is_broken_protocol(u):
        result += u[len(u) // 2]
print(result)
