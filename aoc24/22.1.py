def multiply(a, b):
    return a * b


def mix(a, b):
    return a ^ b


def prune(n):
    return n % 16777216


def divide(a, b):
    return a / b


result = 0
for line in open('22.1.txt').readlines():
    number = int(line.strip())
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
    result += number

print(result)
