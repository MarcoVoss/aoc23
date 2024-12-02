R = []
for line in open("2.1.txt", 'r').readlines():
    R.append([int(r) for r in line.strip().split(" ")])

count = 0
for r in R:
    is_increasing = r[0] < r[1]
    bad = False
    for i in range(len(r) - 1):
        if is_increasing and r[i] >= r[i+1]:
            bad = True
            break
        if not is_increasing and r[i] <= r[i+1]:
            bad = True
            break
        if not (1 <= abs(r[i] - r[i+1]) <= 3):
            bad = True
            break
    if not bad:
        count += 1

print(count)
