lines = open('19.1.txt').readlines()

PATTERNS = lines[0].strip().split(", ")

count = 0
for design in [line.strip() for line in lines[2:]]:
    # find occurrences of each pattern in the design
    found = [[] for _ in range(len(design))]
    for pattern in PATTERNS:
        index = 0
        while True:
            index = design.find(pattern, index)
            if index == -1:
                break
            else:
                found[index].append(len(pattern))
                index += 1

    def find(i: int, found: list[list[int]], seen: set[int]) -> bool:
        if i == len(found):
            return True

        if i in seen:
            return False

        if i >= len(found):
            seen.add(i)
            return False

        for j in found[i]:
            if find(i + j, found, seen):
                return True

        seen.add(i)
        return False

    seen = set()
    if find(0, found, seen):
        count += 1

print(count)
