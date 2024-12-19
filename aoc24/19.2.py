lines = open('19.2.txt').readlines()

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

    def find(i: int, found: list[list[int]], seen: set[int], working: dict[int, int]) -> bool:
        if i == len(found):
            working[i] = 1
            return True

        if i in working:
            return True

        if i >= len(found):
            seen.add(i)
            return False

        if i in seen:
            return False

        yes = False
        for j in found[i]:
            if find(i + j, found, seen, working):
                yes = True
                working.setdefault(i, 0)
                working[i] += working[i + j]
        if not yes:
            seen.add(i)
        return yes

    seen = set()
    working = dict()
    if find(0, found, seen, working):
        count += working[0]
print(count)
