R = 0  # Result
M = 0  # Match
N = ""  # Numbers
for C in open("3.1.txt", 'r').readlines():
    for c in C.strip():
        if c == "m":
            M = 1
        elif c == "u" and M == 1:
            M = 2
        elif c == "l" and M == 2:
            M = 3
        elif c == "(" and M == 3:
            M = 4
        elif (c.isdigit() or c == ",") and M == 4:
            N += c
        elif c == ")" and M == 4:
            a, b = N.split(",")
            R += int(a) * int(b)
            M = 0
            N = ""
        else:
            M = 0
            N = ""

print(R)
