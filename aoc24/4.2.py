
M = [list(m.strip()) for m in open("4.2.txt", 'r').readlines()]

print(sum(
    1
    for i, m in enumerate(M)
    for j, n in enumerate(m)
    if (
        (n == "A") and
        (0 < i < len(M) - 1) and
        (0 < j < len(M[0]) - 1) and
        ("MS" in [f"{M[i+1][j+1]}{M[i-1][j-1]}", f"{M[i-1][j-1]}{M[i+1][j+1]}"]) and
        ("MS" in [f"{M[i+1][j-1]}{M[i-1][j+1]}", f"{M[i-1][j+1]}{M[i+1][j-1]}"])
    )
))
