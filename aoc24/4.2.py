
M = [list(m.strip()) for m in open("4.2.txt", 'r').readlines()]
R = ["X", "M", "A", "S"]


def check(position: tuple[int, int]) -> int:
    y, x = position
    return (
        (0 < y < len(M) - 1) and
        (0 < x < len(M[0]) - 1) and (
            (
                (M[y+1][x+1] == "M" and M[y-1][x-1] == "S") or
                (M[y-1][x-1] == "M" and M[y+1][x+1] == "S")
            ) and
            (
                (M[y+1][x-1] == "M" and M[y-1][x+1] == "S") or
                (M[y-1][x+1] == "M" and M[y+1][x-1] == "S")

            )
        )
    )


count = 0
for i, m in enumerate(M):
    for j, n in enumerate(m):
        if n == "A" and check((i, j)):
            count += 1

print(count)
