

# def foo(a):
#     a[3] = 10
#     return a
#
#
# a = [1, 2, 3, 4, 5]
# print(id(a))
# foo(a)
# print(a)
# print(id(a))


def foo():
    global s
    print(s)
    s = 'local variable'
    print('in foo', s)


s = 'global variable'
print('in main', s)
foo()
print('in main', s)


