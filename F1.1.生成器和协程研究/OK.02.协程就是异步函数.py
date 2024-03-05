from builtins import *

'''
异步函数就是协程
'''


def common_function():
    return 1


def common_generator():
    yield 1


async def async_function():
    # await async_generator()
    return 1


async def async_generator():
    yield 1


# common_function后面不要用(),用了()就是要执行他了。
print(type(common_function))
# output: <class 'function'>

# common_generator()要带(),就是要让他执行，让他产生生成器；否则就是普通的function了。
print(type(common_generator()))
# <class 'generator'>

# 一个函数前面加上关键字async，就是异步函数，也就是协程类型。
print(type(async_function()))
# <class 'coroutine'>

# 异步生成器
print(type(async_generator()))
# <class 'async_generator'>
