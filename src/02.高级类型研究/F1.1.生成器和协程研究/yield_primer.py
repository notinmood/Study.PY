from builtins import *
from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen

    return primer


@coroutine
def get_average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        print("-----")
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    avg = get_average()
    print(type(avg))
    print(getgeneratorstate(avg))
    print(avg.send(10))
    print(avg.send(30))
    print(avg.send(5))
