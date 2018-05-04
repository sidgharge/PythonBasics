import operator

d = {1: 5, 2: 4, 3: 10, 4: 15, 5: 8}

sortedDictAscending = sorted(d.items(), key=operator.itemgetter(1))

print(sortedDictAscending)

sortedDictDescending = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

print(sortedDictDescending)
