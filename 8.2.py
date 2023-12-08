from collections import Counter


instructions = [0 if x == "L" else 1 for x in open("aoc23/8.2.txt", 'r').readlines()[0].strip()]

mapping: dict[str, list[str]] = {}
for x in open("aoc23/8.2.txt", 'r').readlines()[2:]:
    splitted = x.strip().split(" = ")
    mapping[splitted[0]] = splitted[1][1:-1].split(", ")

index = 0
ways = [x for x in mapping.keys() if x.__contains__("A")]

R = []
for way in ways:
    index = 0
    current = way
    while not current.__contains__("Z"):
        current = mapping[current][instructions[index % len(instructions)]]
        index += 1
    R.append(index)

primes = [2, 3]
for x in range(5, len(mapping)):
    if not [t for t in primes if x % t == 0]:
        primes.append(x)

T = {}
for r in R:
    if r in primes and r not in T:
        T[r] = 1
    else:
        p_i = 0
        l = []
        n = r
        while n != 1:
            p = primes[p_i]
            if n % p == 0:
                l.append(p)
                n = int(n / p)
            else:
                p_i += 1
        for k, v in Counter(l).items():
            if T.get(k, 0) < v:
                T[k] = v

result = 1
for k, v in T.items():
    for _ in range(v):
        result *= k

print(result)
