
R = [[int(n) for n in r.split(" ")] for r in open("aoc23/9.2.txt", 'r').readlines()]


def f(r: list[int]) -> int:
    if not any(r) or len(r) == 1:
        return r[0]
    else:
        return r[0] - f([n1 - n0 for n0, n1 in zip(r[:-1], r[1:])])


print(sum(f(r) for r in R))
