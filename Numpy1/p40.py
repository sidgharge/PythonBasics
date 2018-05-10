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
print(np.squeeze(j).shape)
