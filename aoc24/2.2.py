R = []
for line in open("2.2.txt", 'r').readlines():
    R.append([int(r) for r in line.strip().split(" ")])

count = 0
for levels in R:
    bad = False
    j = 0
    while j < len(levels):
        current_levels = levels[:j] + levels[j+1:]
        is_increasing = current_levels[0] < current_levels[1]
        bad = False
        for i in range(len(current_levels) - 1):
            l = current_levels[i]
            r = current_levels[i+1]
            if is_increasing and l >= r:
                j += 1
                bad = True
                break
            if not is_increasing and l <= r:
                j += 1
                bad = True
                break
            if not (1 <= abs(l - r) <= 3):
                j += 1
                bad = True
                break
        if not bad:
            count += 1
            break

print(count)
