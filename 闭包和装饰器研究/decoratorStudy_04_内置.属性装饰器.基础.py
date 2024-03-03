from builtins import *


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 属性装饰器的作用就是将本来需要使用带括号的方法调用，转换为使用不带括号的名称调用（即方法名称后面不再加括号了）。
# +--------------------------------------------------------------------------

class XiaoMing:
    def __init__(self):
        pass

    first_name = '明'
    last_name = '小'

    @property
    def full_name(self):
        return self.last_name + self.first_name

    def get_full_name(self):
        return self.last_name + self.first_name


if __name__ == '__main__':
    xm = XiaoMing()
    # 对一个方法使用了 @property装饰器，就可以直接用属性的方式调用了，而不用按照方法的方式使用（最后要加一个括号这种方法调用的方式）
    print(xm.full_name)
    # 传统方法的调用，最后要加一个括号
    print(xm.get_full_name())
