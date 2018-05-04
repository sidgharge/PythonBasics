import operator

d = {1: 5, 2: 4, 3: 10, 4: 15, 5: 8}

l = (sorted(d.items(), key=operator.itemgetter(0)))

print(l)
