from builtins import *


class XiaoMing:
    def __init__(self):
        pass

    name = '小明'

    @classmethod
    def say_hello(cls):
        print('同学你好， 我是' + cls.name)
        print(cls)


if __name__ == '__main__':
    # 1. 类型方法即可以在类型上调用
    XiaoMing.say_hello()
    # 2. 也可以在实例上调用。都是同样的效果。
    xm = XiaoMing()
    xm.say_hello()

# output--
# 同学你好， 我是小明
# <class '__main__.XiaoMing'>
