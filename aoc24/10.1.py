F: list[list[int]] = []
STARTS = []
for y, line in enumerate(open('10.1.txt').readlines()):
    row = []
    for x, height in enumerate(line.strip()):
        row.append(int(height))
        if int(height) == 0:
            STARTS.append((y, x))
    F.append(row)

D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

scores = []
for start in STARTS:
    score = set()
    current_steps = {start}
    while current_steps:
        next_steps = set()
        for y, x in current_steps:
            h = F[y][x]
            for dy, dx in D:
                if 0 <= y + dy < len(F) and 0 <= x + dx < len(F[0]) and F[y + dy][x + dx] == F[y][x] + 1:
                    if F[y + dy][x + dx] == 9:
                        score.add((y + dy, x + dx))
                    else:
                        next_steps.add((y + dy, x + dx))
        current_steps = next_steps
    scores.append(len(score))
print(sum(scores))
