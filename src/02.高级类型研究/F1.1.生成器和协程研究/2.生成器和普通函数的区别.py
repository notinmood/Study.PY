"""
本代码的使用说明
# 1. 普通函数，调用的时候直接得到返回值
# 2. 生成器函数，调用的时候返回值为一个生成器对象。
#   具体返回值需要使用for循环等形式来迭代获取。
────────────────────────
特别说明：
普通函数内包含yield关键字，则该函数就变成了生成器函数。
"""
from builtins import print


def common_func(a):
    """
    普通函数
    :param a:
    :return:
    """
    print(f"我是普通函数执行的逻辑。传入进来的数据为{a}")
    return a * 2


def yield_func(a):
    """
    生成器函数
    :param a:
    :return:
    """
    print(f"a={a}")
    yield a


if __name__ == '__main__':
    cf = common_func(3)
    print(f"普通函数可以读取到返回值为：{cf}")

    print("-" * 50)

    yf = yield_func(2)
    print(f"yield函数返回值为：{yf}")

# output
# 我是普通函数执行的逻辑。传入进来的数据为3
# 普通函数可以读取到返回值6
# --------------------------------------------------
# yield函数返回值为 < generator object yield_func at 0x000001DCFC1F3430>
