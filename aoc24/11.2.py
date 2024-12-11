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


G: dict[int, int] = {number: 1 for number in numbers}

for turn in range(75):
    NEW_G = {}
    for number, count in G.items():
        for new_number in handle_number(number):
            if new_number not in NEW_G:
                NEW_G[new_number] = 0
            NEW_G[new_number] += count
    G = NEW_G

print(sum(G.values()))
