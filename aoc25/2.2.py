result = 0

for line in open("2.2.txt", 'r').readlines()[0].split(","):
    start, end = line.split("-")
    start = int(start)
    end = int(end)

    for n in range(start, end+1):
        if n < 10:
            continue

        word = str(n)
        a, b = 0, 1
        c, d = 1, 2

        while True:
            if b > len(word) // 2:
                break
            elif word[a:b] == word[c:d]:
                if d == len(word):
                    result += n
                    break
                else:
                    c, d = d, d + (d - c)
            else:
                b += 1
                c, d = b, b + (b - a)


print(result)
