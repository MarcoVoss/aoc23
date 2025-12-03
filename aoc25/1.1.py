l = []
r = []

result = 0
current = 50
for line in open("1.1.txt", 'r').readlines():
    direction = line[0]
    count = int(line[1:])
    if direction == "L":
        current -= count
    else:
        current += count

    current %= 100

    if current == 0:
        result += 1

print(result)
