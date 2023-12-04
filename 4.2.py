content = [line.split(": ")[1] for line in open("aoc23/4.2.txt", 'r').readlines()]

def get_numbers(line: str) -> list[int]:
    return [int(possible_number) for possible_number in line.split(" ") if possible_number != ""]

cards_won = {o_i: 1 for o_i, _ in enumerate(content)}
for o_i, line in enumerate(content):
    numbers = line.split(" | ")
    winning = get_numbers(numbers[0])
    owning = get_numbers(numbers[1])
    own_winning_numbers = list(set(winning) & set(owning))
    for _ in range(cards_won.get(o_i)):
        for d in range(len(own_winning_numbers)):
            cards_won[o_i + d + 1] += 1

print(sum(cards_won.values()))
