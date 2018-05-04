d = {1: 5, 2: 4, 3: 10, 4: 15, 5: 8}

print(sum(d.values()))

mult = 1

for x in d.values():
    mult *= x

print(mult)

d.pop(5)

print(d)
