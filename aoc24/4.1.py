
M = [list(m.strip()) for m in open("4.1.txt", 'r').readlines()]
R = ["X", "M", "A", "S"]


def check(direction: tuple[int, int], position: tuple[int, int]) -> int:
    y, x = position
    dy, dx = direction
    for z in range(4):
        cy = y + z * dy
        cx = x + z * dx
        if cy < 0 or cx < 0 or cy >= len(M) or cx >= len(M[cy]) or M[cy][cx] != R[z]:
            return 0
    return 1


count = 0
for i, m in enumerate(M):
    for j, n in enumerate(m):
        if n == "X":
            count += check((0, 1), (i, j))
            count += check((0, -1), (i, j))
            count += check((1, 0), (i, j))
            count += check((-1, 0), (i, j))
            count += check((1, 1), (i, j))
            count += check((-1, -1), (i, j))
            count += check((1, -1), (i, j))
            count += check((-1, 1), (i, j))

print(count)
