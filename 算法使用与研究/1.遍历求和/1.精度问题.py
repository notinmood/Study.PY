"""
 * @file   : 1.index.py
 * @time   : 上午7:11
 * @date   : 2024/7/18
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from fractions import Fraction

print(1 / 3)
print(1 / 3 + 1 / 3 + 1 / 3)
print("──分割线───────────────────────────────────")

print(1 / 6)
print(1 / 10)
print(1 / 15)
print("──分割线───────────────────────────────────")
print(1 / 10 + 1 / 15 == 1 / 6)
print("──分割线───────────────────────────────────")
print(Fraction(1, 10) + Fraction(1, 15) == Fraction(1, 6))
