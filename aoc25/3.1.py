result = 0

for bank in open("3.1.txt", 'r').readlines():
    bank = str(bank).rstrip()
    a, b = bank[0], bank[1]
    for battery in bank[2:]:
        if int(a) < int(b):
            a = b
            b = 0
        if int(b) < int(battery):
            b = battery
    result += int(f"{a}{b}")

print(result)
