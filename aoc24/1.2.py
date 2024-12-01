l = []
r = []
for line in open("1.2.txt", 'r').readlines():
    _l, _r = line.strip().split("   ")
    l.append(_l)
    r.append(_r)

result = 0
for _l in l:
    result += int(_l) * r.count(_l)

print(result)