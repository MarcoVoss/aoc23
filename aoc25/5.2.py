result = 0

lines = open("5.2.txt", 'r').readlines()

ranges: list[tuple[int, int]] = []
# collect ranges
for ingredient_range in lines:

    if not ingredient_range.strip():
        break

    start, end = map(int, ingredient_range.strip().split("-"))
    ranges.append((start, end))

# merge ranges
merged_ranges = []
while ranges:
    start, end = ranges.pop(0)

    merged = False
    while not merged:
        merged = True
        temp = []
        while len(ranges):
            start_n, end_n = ranges.pop(0)
            if (
                (start <= start_n <= end) or
                (start <= end_n <= end) or
                (start_n <= start <= end_n) or
                (start_n <= end <= end_n)
            ):
                start = min(start, start_n)
                end = max(end, end_n)
                merged = False
            else:
                temp.append((start_n, end_n))
        ranges.extend(temp)

    if merged:
        merged_ranges.append((start, end))


# count ranges
for start, end in merged_ranges:
    result += (end - start) + 1

print(result)
