def multiply(a, b):
    return a * b


def mix(a, b):
    return a ^ b


def prune(n):
    return n % 16777216


def divide(a, b):
    return a / b


result = 0
for line in open('22.2.txt').readlines():
    number = int(line.strip())
    last_digits = [int(str(number)[-1])]
    for _ in range(2000):
        multiplied = multiply(number, 64)
        number = mix(number, multiplied)
        number = prune(number)

        divided = divide(number, 32)
        rounded = int(divided)
        number = mix(number, rounded)
        number = prune(number)

        multiplied = multiply(number, 2048)
        number = mix(number, multiplied)
        number = prune(number)
        last_digits.append(int(str(number)[-1]))

    result += number

print(result)
