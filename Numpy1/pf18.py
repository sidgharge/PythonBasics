
code = 'print("Hello, World")'

exec(code)


def test(a):
    def test2(b):
        nonlocal a
        a += 1
        return a + b
    return test2(2)


def abc(fn, n):
    fn(n)


def abcd(num):
    print(num * num)


abc(abcd, 5)

print(abcd.__code__.co_nlocals)
