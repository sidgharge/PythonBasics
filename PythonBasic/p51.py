import cProfile


def test():
    print('this is a test function')


cProfile.run('test()')
