T = open("aoc23/15.1.txt", 'r').readlines()[0].strip().split(",")

result = 0
for t in T:
    r = 0
    for c in t:
       r += ord(c) 
       r *= 17
       r %= 256
    result += r
print(result)
