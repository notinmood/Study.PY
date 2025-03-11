from builtins import *
from functools import wraps

'''
由于装饰器返回了 wrapper 函数替换掉了之前的 say_hello 函数，因此导致函数名，帮助文档变成了 wrapper 函数的了。
解决这一问题的办法是通过 functools 模块下的 wraps 装饰器。
对，wraps也是一个装饰器，是functools内置的装饰器。
'''


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """doc of wrapper"""
        print('123')
        return func(*args, **kwargs)

    return wrapper


@decorator
def say_hello():
    """doc of say hello"""
    print('同学你好')


print(say_hello.__name__)
print(say_hello.__doc__)

# output-----
# say_hello
# doc of say hello
