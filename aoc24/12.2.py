GARDEN: list[list[str]] = []
DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for line in open('12.2.txt').readlines():
    row = []
    for current_plant in line.strip():
        row.append(current_plant)
    GARDEN.append(row)

seen_plants: set[tuple[int, int]] = set()
groups: list[tuple[int, int]] = []
costs = 0
to_check = [(0, 0)]
while to_check:
    y, x = to_check.pop(0)

    if (y, x) in seen_plants:
        continue

    current_plant = GARDEN[y][x]
    fences = []
    plants = []
    current_group = set()
    plants_to_check = {(y, x)}
    while plants_to_check:
        y, x = plants_to_check.pop()
        current_group.add((y, x))
        plants.append((y, x))
        for dy, dx in DIRECTION:
            cy = y + dy
            cx = x + dx
            if (cy, cx) in current_group:
                continue
            elif not (0 <= cy < len(GARDEN)) or not (0 <= cx < len(GARDEN[0])):
                fences.append((cy, cx))
            elif GARDEN[cy][cx] == current_plant:
                plants_to_check.add((cy, cx))
            else:
                fences.append((cy, cx))
                to_check.append((cy, cx))
    seen_plants.update(current_group)
    groups.append((plants, fences))

    count = 0
    corners = set()
    for y, x in plants:
        ry, rx = DIRECTION[0]
        ly, lx = DIRECTION[1]
        by, bx = DIRECTION[2]
        ty, tx = DIRECTION[3]

        top_is_plant = (y + ty, x + tx) in plants
        bottom_is_plant = (y + by, x + bx) in plants
        left_is_plant = (y + ly, x + lx) in plants
        right_is_plant = (y + ry, x + rx) in plants

        new_corners = []
        if not top_is_plant and not bottom_is_plant and not left_is_plant and not right_is_plant:  # 4 other plants
            new_corners.append(((y + ty, x + tx), (y + ly, x + lx)))
            new_corners.append(((y + ty, x + tx), (y + ry, x + rx)))
            new_corners.append(((y + by, x + bx), (y + ly, x + lx)))
            new_corners.append(((y + by, x + bx), (y + ry, x + rx)))
            count += 4
        elif (
            (top_is_plant and not bottom_is_plant and not left_is_plant and not right_is_plant) or
            (bottom_is_plant and not top_is_plant and not left_is_plant and not right_is_plant) or
            (left_is_plant and not bottom_is_plant and not top_is_plant and not right_is_plant) or
            (right_is_plant and not bottom_is_plant and not left_is_plant and not top_is_plant)
        ):  # 3 other plants
            count += 2
            if top_is_plant:
                new_corners.append(((y + by, x + bx), (y + ly, x + lx)))
                new_corners.append(((y + by, x + bx), (y + ry, x + rx)))
            elif bottom_is_plant:
                new_corners.append(((y + ty, x + tx), (y + ly, x + lx)))
                new_corners.append(((y + ty, x + tx), (y + ry, x + rx)))
            elif left_is_plant:
                new_corners.append(((y + ry, x + rx), (y + ty, x + tx)))
                new_corners.append(((y + ry, x + rx), (y + by, x + bx)))
            elif right_is_plant:
                new_corners.append(((y + ly, x + lx), (y + ty, x + tx)))
                new_corners.append(((y + ly, x + lx), (y + by, x + bx)))
        elif (
            (not top_is_plant and not left_is_plant and bottom_is_plant and right_is_plant) or
            (not top_is_plant and not right_is_plant and bottom_is_plant and left_is_plant) or
            (not bottom_is_plant and not right_is_plant and top_is_plant and left_is_plant) or
            (not bottom_is_plant and not left_is_plant and top_is_plant and right_is_plant)
        ):  # 2 other plants
            count += 1
            if not top_is_plant and not left_is_plant:
                new_corners.append(((y + ty, x + tx), (y + ly, x + lx)))
            elif not top_is_plant and not right_is_plant:
                new_corners.append(((y + ty, x + tx), (y + ry, x + rx)))
            elif not bottom_is_plant and not right_is_plant:
                new_corners.append(((y + by, x + bx), (y + ry, x + rx)))
            elif not bottom_is_plant and not left_is_plant:
                new_corners.append(((y + by, x + bx), (y + ly, x + lx)))

        print((y, x), " -> ", new_corners)

        new_corners = set(tuple(sorted(x, key=lambda x: (x[0], x[1]))) for x in new_corners)
        corners.update(new_corners)
    print(sorted(corners))
    costs += len(plants) * count

print(costs)
