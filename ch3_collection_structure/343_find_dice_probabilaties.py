from collections import Counter, defaultdict

cdict = Counter()
ddict = defaultdict(list)

for d1 in range(1, 6):
    for d2 in range(1, 6):
        t = [d1, d2]
        cdict[d1+d2] += 1
        ddict[d1+d2].append(t)
print(cdict)
print('')
print(ddict)