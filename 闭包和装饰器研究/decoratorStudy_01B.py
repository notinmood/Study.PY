from builtins import *

"""
说明：
    使用@符号修饰的函数func，称为装饰器；
    但无论这个func是否执行，@装饰器内的逻辑都会被调用。
    如下：两个inner_func被@修饰后，都没有主动执行；但@修饰器内部的逻辑都执行了。
"""


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

# if __name__ == '__main__':
# foo = inner_func1(5, 7)
# bar = inner_func2(8, 9)
