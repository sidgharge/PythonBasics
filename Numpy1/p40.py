import numpy as np

x = np.full((3, 5), 2, dtype='int32')
# print(x)

y = np.arange(10, dtype=np.int64)
# print(np.full_like(y, 10, dtype=np.int64))

z = np.eye(3)
# print(z)

a = np.diagflat([1, 2, 3], k=2)
# print(a)

b = np.linspace(2.5, 6.5, 30)
# print(b)

c = np.logspace(2, 5, 20, endpoint=False)
# print(c)

d = np.tri(4, 3, k=-1)
# print(d)

e = np.triu(np.arange(2, 14).reshape((4, 3)), k=-1)
# print(e)

f = np.eye(3)
f = f.flatten()
# print(f)

g = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
# print(g.flat[3])

h = np.array([[1, 2, 3]])
# print(np.swapaxes(h, 0, 1))

i = np.random.randint(1, 5, (3, 2))
# print(i)
# print(np.moveaxis(i, 0, 1))

j = np.random.randint(1, 5, (2, 2))
# print(j)
j = np.expand_dims(j, axis=0)
# print(j)

j = np.random.randint(1, 5, (2, 2, 2))
# print(np.squeeze(j).shape)

k = np.array([[1, 2, 3], [4, 5, 6]])
l = np.array([[7, 8, 9], [10, 11, 12]])
# print(np.concatenate((k, l), axis=1))

m = np.array([10, 20, 30])
n = np.array([40, 50, 60])
# print(np.column_stack((m, n)))

o = np.arange(14)
# print(np.split(o, [2, 6]))

p = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11],
              [12, 13, 14, 15]])
# print(np.split(p, 2, axis=1))

q = np.array([[0, 10, 20],
              [20, 30, 40]])
# print(np.count_nonzero(q))

r = np.zeros((5, 5))
r += np.arange(5)
# print(r)

s = np.array([[1.12, 2.0, 3.45], [2.33, 5.12, 6.0]])
# print(2.33 in s)

t = np.linspace(0, 1, 11, dtype=np.float, endpoint=False)[1:]
# print(t)

u = np.ones(5)
u.flags.writeable = False
# u[1] = 5

v = np.arange(100)
w = v[(v % 3 == 0) | (v % 5 == 0)]
# print(w)
# print(np.sum(w))
