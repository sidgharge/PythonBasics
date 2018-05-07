# import numpy as np
#
# a = np.array([10, 20])
#
# print(a.repeat(2))

import time as t

string = 'hello' * 10000

d = {}

start = t.time()

for s in string:
    d[s] = string.count(s)

end = t.time()
print(d)
print(end - start)

e = {}

start1 = t.time()

for s in string:
    # v = e.get(s)
    if e.get(s) is None:
        e[s] = 1
    else:
        e[s] = e[s] + 1

end1 = t.time()

print(e)
print(end1 - start1)

f = {}

start2 = t.time()

for s in string:
    v = f.get(s)
    if v is None:
        f[s] = 1
    else:
        f[s] = v + 1

end2 = t.time()

print(f)
print(end2 - start2)

