a = ()
b = tuple()
c = ('hello', 'world')
# print(a, b, c)

d = ('hello', 5, 10.5)
# print(d)

e = 1, 5, 12
# print(e)

f = 6,
# print(f)

g, h, i = e
# print(g, h, i)

j = e + (15,)
# print(j)

k = ('h', 'e', 'l', 'l', 'o')
# print(''.join(k))

l = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print('Fourth El: ', l[3], '\nFourth from last: ', l[-4])

m = 2, 4, 5, 6, 2, 3, 4, 7
# print(m.count(4))

# print(5 in m)

n = [2, 4, 5, 6, 2, 3, 4, 7]
# print(tuple(n))

o = ('h', 'e', 'l', 'l', 'o')
# o = o[1:]
# print(o)

# print(o.index('e'))

# print(len(o))

p = ((2, "w"), (3, "r"))
q = dict((x, y) for x, y in p)
# print(q)

r = tuple(reversed(o))
# print(r)

s = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
t = {}
for a, b in s:
    t.setdefault(a, []).append(b)
# print(t)

u = (100, 200, 300)
# print('This is a tuple {}'.format(u))

v = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print([a[:-1] + (100,) for a in v])

w = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# print(sorted(w, key=lambda x: float(x[1]), reverse=True))

x = [10, 20, 30, (10, 20), 40]
count = 0
for n in x:
    if isinstance(n, tuple):
        break
    count += 1
print(count)
