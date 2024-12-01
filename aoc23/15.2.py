T = open("aoc23/15.2.txt", 'r').readlines()[0].strip().split(",")

B: dict[int, dict] = {i: {} for i in range(256)}
for j, t in enumerate(T):
    b = 0
    l = ""
    for i, c in enumerate(t):
        if c not in ["-", "="]:
            b += ord(c) 
            b *= 17
            b %= 256
            l += c
        else:
            if c == "-":
                B[b]
                try:
                    del B[b][l]
                except Exception:
                    pass
            else:
                B[b][l] = int(t[i+1:])
            break

print(sum([
    (number + 1) * (position + 1) * focal
    for number, box in B.items()
    for position, focal in enumerate(box.values())
]))