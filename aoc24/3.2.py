R = 0  # Result
M = 0  # Match
A = True
DO = 0
DONT = 0
N = ""  # Numbers
for C in open("3.2.txt", 'r').readlines():
    for c in C.strip():
        if c == "d":
            DO = 1
            DONT = 1
        elif c == "o" and DO == 1:
            DO = 2
            DONT = 2
        elif c == "(" and DO == 2:
            DO = 3
        elif c == ")" and DO == 3:
            DO = 0
            A = True
        elif c == "n" and DONT == 2:
            DO = 0
            DONT = 3
        elif c == "'" and DONT == 3:
            DONT = 4
        elif c == "t" and DONT == 4:
            DONT = 5
        elif c == "(" and DONT == 5:
            DONT = 6
        elif c == ")" and DONT == 6:
            DONT = 0
            A = False
        elif c == "m":
            M = 1
        elif c == "u" and M == 1:
            M = 2
        elif c == "l" and M == 2:
            M = 3
        elif c == "(" and M == 3:
            M = 4
        elif (c.isdigit() or c == ",") and M == 4:
            N += c
        elif c == ")" and M == 4 and A:
            a, b = N.split(",")
            R += int(a) * int(b)
            M = 0
            N = ""
        else:
            M = 0
            N = ""
            DO = 0
            DONT = 0

print(R)
