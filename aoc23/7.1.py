hands = [line.split(" ") for line in open("aoc23/7.1.txt", 'r').readlines()]

mapping = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
}

hands = [
    ([mapping.get(card) for card in hand], int(bid))
    for (hand, bid) in hands
]

def rate_hand(hand: list) -> int:
    unique = set(hand)
    if len(unique) == 1:
        return 6
    if len(unique) == 2:
        tmp = [x for x in hand]
        for x in unique:
            tmp.remove(x)
        if len(set(tmp)) == 1:
            return 5
        return 4
    if len(unique) == 3:
        tmp = [x for x in hand]
        for x in unique:
            tmp.remove(x)
        if len(set(tmp)) == 1:
            return 3
        return 2
    if len(unique) == 4:
        return 1
    return 0

rated_hands = [(*hand, rate_hand(hand[0])) for hand in hands]

sorted_hands = sorted(rated_hands, key=lambda x: (x[2], -x[0][0], -x[0][1], -x[0][2], -x[0][3], -x[0][4]))

print(sum([
    bid * (index + 1) for index, (_, bid, _) in enumerate(sorted_hands)
]))
