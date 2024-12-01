times = [number for number in open("aoc23/6.2.txt", 'r').readlines()[0].split(": ")[1].strip().split(" ") if number]
distances = [number for number in open("aoc23/6.2.txt", 'r').readlines()[1].split(": ")[1].strip().split(" ") if number]

time = int("".join(times))
distance = int("".join(distances))

def get_numbers_to_win(time: int, distance: int) -> int:
    for t in range(time-1, 1, -1):
        if (time - t) * t > distance:
            return t - (time - t) + 1


print(get_numbers_to_win(time=time, distance=distance))
