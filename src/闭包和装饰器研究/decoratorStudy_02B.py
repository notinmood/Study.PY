from builtins import *


def padding_func(level=0):
    def outer_func(fn):
        print("我是outer内的逻辑")

        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=level, func=fn.__name__))
            return fn(*args, **kwargs)

        return wrapper

    return outer_func


@padding_func(2)
def inner_func(a, b):
    print(f"传递进来的参数为{a},{b}")


if __name__ == '__main__':
    inner_func(5, 7)
