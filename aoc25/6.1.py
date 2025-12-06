result = 0

lines = open("6.1.txt", 'r').readlines()
operations = list(lines.pop().strip().replace(" ", ""))
problems = [None for _ in range(len(operations))]

for line in lines:
    numbers = [part for part in line.strip().split(" ") if part.isdigit()]
    for index, number in enumerate(map(int, numbers)):
        print(number)
        if problems[index] is None:
            problems[index] = number
        elif operations[index] == "*":
            problems[index] *= number
        else:
            problems[index] += number

print(sum(problems))
