"""
 * @file   : 1.index.py
 * @time   : 上午7:11
 * @date   : 2024/7/18
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from fractions import Fraction
from itertools import product


def double_loop():
    """
    使用双重循环求解1/6=1/i+1/j=1/6的解集
    :return:
    """
    solutions = []
    for i in range(1, 100):
        for j in range(i, 100):
            if Fraction(1, i) + Fraction(1, j) == Fraction(1, 6):
                solutions.append((i, j))
            pass
        pass
    pass

    print(solutions)
    # --output---
    # [(7, 42), (8, 24), (9, 18), (10, 15), (12, 12)]


def using_product():
    """
    使用itertools.product()笛卡尔积函数求解1/6=1/i+1/j=1/6的解集
    :return:
    """
    solutions = []
    for i, j in product(range(1, 100), range(1, 100)):
        if Fraction(1, i) + Fraction(1, j) == Fraction(1, 6):
            if (i, j) not in solutions and (j, i) not in solutions:
                solutions.append((i, j))
            pass
        pass
    pass

    print(solutions)
    # --output---
    # [(7, 42), (8, 24), (9, 18), (10, 15), (12, 12)]


pass

# 遍历求和
if __name__ == '__main__':
    # 使用双重循环求解
    double_loop()
    print("──分割线───────────────────────────────────")
    # 使用itertools.product()笛卡尔积函数求解
    using_product()
