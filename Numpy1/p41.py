import numpy as np

a = np.arange(1e3)
# print(a)

b = np.arange(15).reshape((3, 5))
# for i in np.nditer(b):
#     print(i, end=' ')

c = np.arange(15).reshape((3, 5))
# for i in np.nditer(c, order='F'):
#     print(i, end=' ')

d = np.ones((5, 5, 5), dtype=np.int)
# print(d)

e = np.arange(12).reshape(3, 4)
# print(e * 3)

f = np.arange(4)
g = np.arange(8).reshape(2, 4)
# for a, b in np.nditer([f, g]):
#     print(a, ':', b)

h = np.zeros(3, dtype=('i4,f4,a40'))
i = [(1, 2., "Albert Einstein"), (2, 2., "Edmond Halley"), (3, 3., "Gertrude B. Elion")]
h[:] = i


# print(h)


def cube_array(arr):
    return arr ** 3


j = np.arange(1, 4)
# print(cube_array(j))

k = np.arange(12).reshape(3, 4)
# for a in np.nditer(k, flags=['external_loop'], order='F'):
#     print(a)

l = np.array([1, 2, 3, 4])
m = np.array(['Red', 'Green', 'White', 'Orange'])
n = np.array([12.20, 15, 20, 40])
res = np.core.records.fromarrays([l, m, n])
# print(res[0])
# print(res[1])
# print(res[2])

o = np.arange(10).reshape(5, 2)
# print(o.tolist())

p = np.arange(6).reshape(3, 2)
# print(p[0, :])
# print(p[1, :])
# print(p[2, :])

q = np.array([[12.0, 12.51], [2.34, 7.98], [25.23, 36.50]])
# print(q.astype(np.int))

r = np.array([0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349,
              0.35399976, 0.99469633, 0.0694458, 0.54711478])
# np.set_printoptions(precision=3)
# print(r)

s = np.array([1.6e-10, 1.6, 1200, .235])
# np.set_printoptions(suppress=True)
# print(s)

iterable = (a for a in np.arange(10))
t = np.fromiter(iterable, dtype=np.int)
# print(t)

u = np.array([[10, 20, 30], [40, 50, 60]])
v = np.array([[100], [200]])
# print(np.append(u, v, axis=1))

w = np.array([[20, 20, 20, 0],
              [0, 20, 20, 20],
              [0, 20, 20, 20],
              [20, 20, 20, 0],
              [10, 20, 20, 20]])
# print(np.unique(w, axis=0))

x = np.array([[1, 2, 3], [4, 5, np.nan], [7, 8, 9], [True, False, True]])
# print(x[~np.isnan(x).any(axis=1)])

y = np.array([[20, 20, 20], [30, 30, 30], [40, 40, 40]])
z = np.array([20, 30, 40])
print(y / z[:, None])
