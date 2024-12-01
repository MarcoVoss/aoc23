T = [l.strip().split(" ") for l in open("aoc23/12.1.txt", 'r').readlines()]
S = [(s, [int(i) for i in k.split(",") ],) for s, k in T]


def solve(s: str, l: list[int], i: int = 0, j: int = 0) -> int:
    # print("S", s[:j], s[j:], i, j)
    if i == len(l):
        if "#" not in s[j:]:
            # print("1")
            return 1
        # print("0.1")
        return 0
    
    if j == len(s):
        # print("0.2")
        return 0
    
    t = "".join("#" for _ in range(l[i]))
    n = j + (s[j:].find("#") if "#" in s[j:] else len(s[j:]))
    k = s.replace("?", "#")
    c = 0

    while j <= n:
        # print("W", k[:j], k[j:], t, j, n)
        if (
            (j - 1 < 0 or j - 1 >= len(s) or s[j-1] in [".", "?"]) and
            k[j:].startswith(t) and
            (j + l[i] < 0 or j + l[i] >= len(s) or s[j + l[i]] in [".", "?"])            
        ):
            c += solve(s, l, i+1, j + l[i] + 1)
        j += 1
    return c

# for s in S:
#     print(s, solve(*s))

print(sum(solve(*s) for s in S))
