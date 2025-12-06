result = 0

lines = open("6.2.txt", 'r').readlines()
operations = lines.pop()

i = 0
while i < len(operations):
    j = i

    numbers = []
    str_number = "".join(line[j] for line in lines).strip()
    while str_number:
        numbers.append(int(str_number))
        j += 1
        if j == len(operations):
            break
        str_number = "".join(line[j] for line in lines).strip()

    sub_result = numbers[0]

    if operations[i] == "*":
        for number in numbers[1:]:
            sub_result *= number
    else:
        for number in numbers[1:]:
            sub_result += number

    result += sub_result
    i = j+1

print(result)
