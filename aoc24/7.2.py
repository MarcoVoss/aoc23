
M: list[int, list[int]] = []

for line in open('7.2.txt').readlines():
    result, equation = line.strip().split(":")
    numbers = equation.strip().split(" ")
    M.append((int(result), list(map(int, numbers))))


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


METHODS = [add, multiply, concat]


def is_possible(result: int, numbers: list[int]) -> int:
    L = len(numbers) - 1
    K = [0 for _ in range(L)]
    while True:
        def calculate(j: int):
            if j == 0:
                return numbers[j]
            return METHODS[int(K[j-1])](calculate(j-1), numbers[j])

        if calculate(L) == result:
            return result

        if sum(K) == L*(len(METHODS)-1):
            return 0

        for i, k in enumerate(K):
            K[i] = (k + 1) % len(METHODS)
            if K[i] == k + 1:
                break


print(sum(is_possible(result, equation) for result, equation in M))
