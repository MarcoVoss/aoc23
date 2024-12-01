numbers_per_row = [
    [char for char in line if char.isnumeric()]
    for line in open("aoc23/1.1.txt", 'r').readlines()
]

summed_numbers = [
    int(f"{row[0]}{row[-1]}")
    for row in numbers_per_row
]

print(sum(summed_numbers))
