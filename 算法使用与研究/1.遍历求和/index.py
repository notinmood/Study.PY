"""
 * @file   : 1.index.py
 * @time   : 上午7:11
 * @date   : 2024/7/18
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from fractions import Fraction

# 遍历求和
if __name__ == '__main__':
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
