from utils import LeftJoin, read_lines


l = []
r = []
for line in open("1.1.txt", 'r').readlines():
    _l, _r = line.strip().split("   ")
    l.append(_l)
    r.append(_r)

l = sorted(l)
r = sorted(r)

result = sum([abs(int(l[i]) - int(r[i])) for i in range(len(l))])

print(result)

# Testing


class Left(Table):
    value: int


class Right(Table):
    value: int


Select(

)


left = []
right = []
lines = read_lines("1.1.txt")
for x in lines:
    l, r = x.strip().split("   ")
    left.append(l)
    right.append(r)

connection = LeftJoin(left, right)
