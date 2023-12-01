number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

numbers = list(number_map.keys()) + list(number_map.values())

result = 0
for line in open("aoc23/1.2.txt", 'r').readlines():
    T = [(index, text) for text in numbers if (index := line.find(text)) != -1]
    T = sorted(T, key=lambda x:x[0])
    first = number_map.get(T[0][1], T[0][1])

    T = [(index, text) for text in numbers if (index := line.rfind(text)) != -1]
    T = sorted(T, key=lambda x:x[0], reverse=True)
    second = number_map.get(T[0][1], T[0][1])

    result += int(f"{first}{second}")


print(result)
