from builtins import *
from inspect import getgeneratorstate


def get_average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    avg = get_average()
    print(avg.send(None))
    print(avg.send(10))
    print(avg.send(20))
    # 用close方法可以将yield停止
    avg.close()
    print(getgeneratorstate(avg))

    # 如果yield已经停止了，再次调用的时候，就会抛出异常
    print(avg.send(20))
