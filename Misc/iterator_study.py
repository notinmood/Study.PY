from builtins import *


def add(s, x):
    return s + x


def gen():
    for i in range(4):
        yield i


if __name__ == '__main__':
    myGen = gen()
    # for n in [1, 10]:
    #     base = (add(i, n) for i in myGen)
    #     # base = (add(i, n) for i in gen())
    #
    # print(list(base))

    base = (add(i, 2) for i in myGen)
    print(list(base))
