T = [(x, []) for t in open("aoc23/17.1.txt", 'r').readlines() for x in t.strip()]


e = (len(T)-1, len(T[0])-1)
C = [(0, 0)]
