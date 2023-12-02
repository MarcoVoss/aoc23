games = {
    index + 1 : line.split(":")[1]
    for index, line in enumerate(open("aoc23/2.1.txt", 'r').readlines())
}

sets = {
    index : game.split(";")
    for index, game in games.items()
}

def get_amx_for_color(sets: list[str], color: str) -> int:
    return max([int(entry.strip().split(" ")[0]) for set in sets for entry in set.split(", ") if entry.__contains__(color)])

max_sets = {
    index : {
        "red": get_amx_for_color(sets, "red"),
        "blue": get_amx_for_color(sets, "blue"),
        "green": get_amx_for_color(sets, "green"),
    }
    for index, sets in sets.items()
}

survived_games = [
    index
    for index, information in max_sets.items()
    if (
        information.get("red") <= 12 and
        information.get("blue") <= 14 and
        information.get("green") <= 12
    )
]

print(sum(survived_games))
