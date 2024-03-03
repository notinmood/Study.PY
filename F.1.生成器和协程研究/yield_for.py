from builtins import *


def func():
    for x in 'AB':
        yield x

    for x in range(0, 3):
        yield x


if __name__ == '__main__':
    print(list(func()))
    print(tuple(func()))

