result = 0

lines = list(map(list, open("7.1.txt", 'r').readlines()))

for i, line in enumerate(lines):
    if i == 0:
        continue
    for j, char in enumerate(line):
        if lines[i-1][j] in ["|", "S"]:
            if char == "^":
                result += 1
                if j > 0 and line[j-1] == ".":
                    line[j-1] = "|"
                if j+1 < len(line) and line[j+1] == ".":
                    line[j+1] = "|"
            else:
                line[j] = "|"

print(result)
