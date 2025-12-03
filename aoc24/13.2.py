F: list[list[int]] = []

lines = open('13.2.txt').readlines()
costs = 0
A = 3
B = 1
i = 0
while i < len(lines):
    ax, ay = lines[i].split(":")[1].strip().split(", ")
    bx, by = lines[i+1].split(":")[1].strip().split(", ")
    px, py = lines[i+2].split(":")[1].strip().split(", ")
    ax = int(ax[2:])
    ay = int(ay[2:])
    bx = int(bx[2:])
    by = int(by[2:])
    px = int(px[2:]) + 10000000000000
    py = int(py[2:]) + 10000000000000

    # px = n*bx + m*ax
    # py = n*by + m*ay

    bn = px // bx
    while bn >= 0:
        dx = px - bn * bx
        if dx % ax == 0:
            dy = py - bn * by
            an = dx // ax
            if dy == an * ay:
                costs += bn * B
                costs += dx // ax * A
                break
        bn -= 1

    i += 4

print(costs)
