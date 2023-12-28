T = []
for line in open("aoc23/24.1.txt", 'r').readlines():
    line = line.strip()
    position, velocity = line.split(" @ ", 1)
    px, py, _ = position.split(", ")
    vx, vy, _ = velocity.split(", ")
    b = int(py) - (int(vy) / int(vx) * int(px))
    T.append((int(py), int(vy), int(vx), int(px), b))

r = 0
for i in range(len(T)):
    for j in range(i+1, len(T)):
        y1, vy1, vx1, x1, b1 = T[i]
        y2, vy2, vx2, x2, b2 = T[j]

        bd = (b2 - b1)
        md = (vy1 / vx1 - vy2 / vx2)

        if md == 0 and bd == 0:
            r += 1
        elif md == 0:
            pass # parallel
        else:
            x = bd / md
            y = vy1 / vx1 * x + b1

            if (
                ((vx1 > 0 and x >= x1) or (vx1 < 0 and x <= x1)) and
                ((vx2 > 0 and x >= x2) or (vx2 < 0 and x <= x2)) and
                ((vy1 > 0 and y >= y1) or (vy1 < 0 and y <= y1)) and
                ((vy2 > 0 and y >= y2) or (vy2 < 0 and y <= y2)) and
                (200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000)
            ):
                r += 1

print(r)
