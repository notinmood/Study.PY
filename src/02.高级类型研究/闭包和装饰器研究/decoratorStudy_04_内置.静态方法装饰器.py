from builtins import *


class XiaoMing:
    def __init__(self):
        pass

    @staticmethod
    def say_hello():
        print('同学你好')


if __name__ == '__main__':
    # 1. 静态方法即可以在类型上调用
    XiaoMing.say_hello()
    # 2. 也可以在实例上调用。都是同样的效果。
    xm = XiaoMing()
    xm.say_hello()


# output----
# 同学你好
# 同学你好
