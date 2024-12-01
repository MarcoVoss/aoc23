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