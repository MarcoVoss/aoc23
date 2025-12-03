GARDEN: list[list[str]] = []
DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for line in open('12.1.txt').readlines():
    row = []
    for current_plant in line.strip():
        row.append(current_plant)
    GARDEN.append(row)

seen_plants: set[tuple[int, int]] = set()
groups: list[tuple[int, int]] = []
to_check = [(0, 0)]
while to_check:
    y, x = to_check.pop(0)

    if (y, x) in seen_plants:
        continue

    current_plant = GARDEN[y][x]
    fences = 0
    plants = 0
    current_group = set()
    plants_to_check = {(y, x)}

    while plants_to_check:
        y, x = plants_to_check.pop()
        current_group.add((y, x))
        plants += 1
        for dy, dx in DIRECTION:
            cy = y + dy
            cx = x + dx
            if (cy, cx) in current_group:
                continue
            elif not (0 <= cy < len(GARDEN)) or not (0 <= cx < len(GARDEN[0])):
                fences += 1
            elif GARDEN[cy][cx] == current_plant:
                plants_to_check.add((cy, cx))
            else:
                fences += 1
                to_check.append((cy, cx))
    seen_plants.update(current_group)
    groups.append((plants, fences))

print(sum(plants * fences for plants, fences in groups))
