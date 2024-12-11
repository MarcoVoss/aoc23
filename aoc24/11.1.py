F: list[list[int]] = []

data = open('11.2.txt').readlines()[0]
numbers = [int(d) for d in data.strip().split(" ")]


def handle_number(number: int) -> list[int]:
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        string = str(number)
        middle = len(string) // 2
        return [int(string[:middle]), int(string[middle:])]
    else:
        return [number * 2024]


for _ in range(25):
    new_numbers = []
    for number in numbers:
        for new_number in handle_number(number):
            new_numbers.append(new_number)
    numbers = new_numbers
print(len(numbers))
