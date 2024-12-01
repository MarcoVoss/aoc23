content = [line.split(": ")[1] for line in open("aoc23/4.1.txt", 'r').readlines()]

def get_numbers(line: str) -> list[int]:
    return [int(possible_number) for possible_number in line.split(" ") if possible_number != ""]

result = 0
for line in content:
    numbers = line.split(" | ")
    winning = get_numbers(numbers[0])
    owning = get_numbers(numbers[1])
    line_result = 0
    own_winning_numbers = list(set(winning) & set(owning))
    if own_winning_numbers:
        line_result = 0.5
    for winning_number in own_winning_numbers:
        line_result *= 2
    result += int(line_result)

print(result)
