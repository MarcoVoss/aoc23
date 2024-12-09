F: list[str] = []
p: int = 0

line = open('9.1.txt').readlines()[0]
for i, n in enumerate(line.strip()):
    if i % 2 == 0:
        k = p
        p += 1
    else:
        k = "."
    for _ in range(int(n)):
        F.append(k)


j = len(F) - 1
for i in range(len(F)):
    if j <= i:
        break
    if F[i] == ".":
        while F[j] == "." and j > 0:
            j -= 1
        F[i] = F[j]
        F[j] = "."
        j -= 1

C = 0
for i, n in enumerate(F):
    if F[i] != ".":
        C += i * int(n)
print(C)
