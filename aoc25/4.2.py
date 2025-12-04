result = 0

M = []

for positions in open("4.2.txt", 'r').readlines():
    M.append(list(positions.strip()))

removed = True

while removed:
    removed = False
    for x, row in enumerate(M):
        for y, position in enumerate(row):
            if position == "@":
                paper = 0
                for dx in [1, 0, -1]:
                    for dy in [1, 0, -1]:
                        if (
                            (dx != 0 or dy != 0) and
                            (0 <= x + dx < len(M)) and
                            (0 <= y + dy < len(row)) and
                            (M[x+dx][y+dy] == "@")
                        ):
                            paper += 1
                if paper < 4:
                    M[x][y] = "."
                    result += 1
                    removed = True


print(result)
