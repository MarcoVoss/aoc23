T = [list(l.strip()) for l in open("aoc23/14.1.txt", 'r').readlines()]
T = [t[::-1] for t in (zip(*T[::-1]))]

r = 0
for t in T:
    j = 0
    for i in range(len(t)):
        if t[i] == "#":
            j = i + 1
        elif t[i] == "O":
            r += len(t) - j
            j += 1
print(r)
