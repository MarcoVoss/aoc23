times = [int(number) for number in open("aoc23/6.1.txt", 'r').readlines()[0].split(": ")[1].strip().split(" ") if number]
distances = [int(number) for number in open("aoc23/6.1.txt", 'r').readlines()[1].split(": ")[1].strip().split(" ") if number]


def get_numbers_to_win(time: int, distance: int) -> int:
    for t in range(time-1, 1, -1):
        if (time - t) * t > distance:
            return t - (time - t) + 1


def multiply(numbers: list[int]):
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return result


print(multiply([get_numbers_to_win(time=time, distance=distances[index])for index, time in enumerate(times)]))
