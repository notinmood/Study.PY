from builtins import *

'''
如果是嵌套函数的时候，内部函数使用外部函数的自由变量的时候，
使用global就不合适了，这个时候有另外一个关键字nonlocal
'''


def outer():
    y = 100

    def inner():
        nonlocal y
        y = 200
        print("在inner中展示y的值为{}".format(y))

    inner()
    print("在outer中展示y的值为{}".format(y))


if __name__ == '__main__':
    outer()

# output
# 在inner中展示y的值为200
# 在outer中展示y的值为200
