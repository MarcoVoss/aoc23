l = []
r = []

result = 0
current = 50
for line in open("1.2.txt", 'r').readlines():
    direction = line[0]
    count = int(line[1:])

    if direction == "L":
        operator = -1
    else:
        operator = 1

    # ich war zu dumm für ne Berechnung. Take this
    for _ in range(count):
        current += (1 * operator)

        if 0 < current <= 99:
            continue
        elif current == 0:
            result += 1
        elif current == -1:
            current = 99
        elif current == 100:
            current = 0
            result += 1

print(result)
