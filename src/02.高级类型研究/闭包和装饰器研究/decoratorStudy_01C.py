from builtins import *


def outer_func_wrapper(fn):
    print("YES-对内部函数进行包装，然后返回的方式")

    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


def outer_func_directly(fn):
    """
    对内部函数不进行包装，直接返回的方式
    :param fn:
    :return:
    """
    print("NO-对内部函数不进行包装，直接返回的方式")
    return fn


pass


@outer_func_wrapper
def inner_func1(a, b):
    print(f"传递进来的参数为{a},{b}")


@outer_func_directly
def inner_func2(a, b):
    print(f"传递进来的参数为{a},{b}")


if __name__ == '__main__':
    """
    从以下演示中，似乎未使用 wrapper包装的装饰器效果更好：
    因为，被修饰的函数的参数都可以正常体现在代码提示里面。
    """
    foo = inner_func1(5, 7)
    bar = inner_func2(8, 9)
