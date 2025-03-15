from builtins import *

'''
一个函数不止有他的执行语句，还有着 __name__（函数名），__doc__ （说明文档）等属性，
使用装饰器缺省情况下会导致这些属性改变。
'''


def decorator(func):
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
# wrapper
# doc of wrapper
