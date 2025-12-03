result = 0

for line in open("2.1.txt", 'r').readlines()[0].split(","):
    start, end = line.split("-")
    start = int(start)
    end = int(end)

    # find inner ranges with even number of digits
    current = start

    while current < end:
        length = len(str(current))
        if length % 2 != 0:
            current = int(f"1{'0' * length}")
        else:
            possible_end = int(f"1{'0' * length}")
            for n in range(current, min(possible_end, end + 1)):
                left = str(n)[:length//2]
                right = str(n)[length//2:]
                if left == right:
                    result += n
            current = int(f"{possible_end}0")

print(result)
