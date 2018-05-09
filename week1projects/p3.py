
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']

l3 = []
for x, y in zip(l1, l2):
    temp = [x, y]
    l3.append(temp)

print(l3)


def add_arrays(list1, list2):
    return [[x1, y1] for x1, y1 in zip(list1, list2)]


print(add_arrays(l1, l2))

