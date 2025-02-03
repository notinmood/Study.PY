"""
 * @file   : example.py
 * @time   : 19:04
 * @date   : 2024/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# example.py
def add(a: int, b: int) -> int:
    return a + b

# 以下是为了消除ide参数未使用的警告而做的PolyFill
# noinspection all
result = add(1, "2")  # ←这里会有类型错误
