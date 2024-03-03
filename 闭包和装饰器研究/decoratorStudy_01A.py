from builtins import *

"""
普通的装饰器
"""


def inner_func(a, b):
    print(f"给内部函数传递进来的参数为{a},{b}")


def outer_func_directly(fn):
    """
    对内部函数不进行包装，直接返回的方式
    :param fn:
    :return:
    """
    print("NO-对内部函数不进行包装，直接返回的方式")
    return fn


pass


def outer_func_wrapper(fn):
    print("YES-对内部函数进行包装，然后返回的方式")

    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


pass

if __name__ == '__main__':
    #  直接返回内部函数的方式更好，其参数的性质没有改变
    bar = outer_func_directly(inner_func)
    bar(a=5, b=9)

    #  包装内部函数的方式，其参数的性质发生了改变
    foo = outer_func_wrapper(inner_func)
    foo(5, 7)
