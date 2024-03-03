"""
 * @file   : yield_from.py
 * @time   : 7:31
 * @date   : 2024/2/19
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
#     yield from 后面可以是 迭代器， 生成器， 或者是 包含yield的生成器函数
#     yield from 后面还可以是 一个包含多个yield的生成器函数
#     yield from 后面还可以是 一个列表， 元组
#     yield from 后面还可以是 一个字典
#     yield from 后面还可以是 一个集合
# +--------------------------------------------------------------------------

def func1():
    """
    调用yield from 的主语句
    :return:
    """
    yield 1
    yield from func2()
    yield from (5, 6)
    yield from {'a': 1, 'b': 2}
    yield from {'a': 1, 'b': 2}.values()
    yield from {'a': 1, 'b': 2}.items()
    yield from {'a': 1, 'b': 2}.keys()
    yield from ["A", "B", "C"]
    yield 2


def func2():
    """
    被yield from 调用的子语句
    :return:
    """
    yield 3
    yield 4


if __name__ == '__main__':
    f1 = func1()
    for item in f1:
        print(item)
    pass
