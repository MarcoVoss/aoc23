result = 0

lines = open("5.1.txt", 'r').readlines()

ranges: list[tuple[int, int]] = []
i = 0
while i < len(lines):
    ingredient_range = lines[i]

    if not ingredient_range.strip():
        i += 1
        break

    start, end = map(int, ingredient_range.strip().split("-"))
    ranges.append((start, end))

    i += 1

for ingredient_id in lines[i:]:
    for start, end in ranges:
        if start <= int(ingredient_id) <= end:
            result += 1
            break

print(result)
