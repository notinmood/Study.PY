"""
 * @file   : 5.partial偏函数的使用.py
 * @time   : 下午7:08
 * @date   : 2024/8/21
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import functools


# 原始函数
def add(x, y, z):
    return x + y + z


# 创建偏函数
add_1 = functools.partial(add, 1)
add_10 = functools.partial(add, 10)
add_2_6 = functools.partial(add, 2, 6)

# 调用偏函数
print(add_1(2, 3))  # 6
print(add_10(2, 3))  # 15
print(add_2_6(3))  # 11
