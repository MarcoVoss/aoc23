result = 0

for bank in open("3.2.txt", 'r').readlines():
    bank = list(map(int, str(bank).rstrip()))
    active = list(bank[:12])

    left_end = 0
    for active_battery_index in range(12):
        best_index = left_end
        left_batteries = (12 - (active_battery_index + 1))

        for next_battery_index in range(left_end + 1, len(bank) - left_batteries):
            if bank[best_index] < bank[next_battery_index]:
                best_index = next_battery_index

        step = best_index - left_end

        if step:
            for index, battery_to_move in enumerate(range(active_battery_index, 12)):
                active[battery_to_move] = bank[left_end + index + step]

            left_end += step

        left_end += 1
    result += int("".join(map(str, active)))

print(result)
