from builtins import *

'''
带参数的装饰器
'''


def inner_func(a, b):
    print(f"传递进来的参数为{a},{b}")


def padding_func(level=0):
    def outer_func(fn):
        print("我是outer内的逻辑")

        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=level, func=fn.__name__))
            return fn(*args, **kwargs)

        return wrapper

    return outer_func


if __name__ == '__main__':
    """
    以下代码中，
    padding_func(1)这一步是得到outer_func这个函数；
    padding_func(1)(inner_func)这一步得到的是wrapper这个函数
    padding_func(1)(inner_func)(5, 7)这一步得到的是inner_func的执行结果
    """
    foo = padding_func(1)(inner_func)(5, 7)
