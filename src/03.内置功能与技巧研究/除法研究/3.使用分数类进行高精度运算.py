"""
 * @file   : 3.使用分数类进行高精度控制.py
 * @time   : 17:35
 * @date   : 2025/2/3
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import fractions

if __name__ == '__main__':
    a = fractions.Fraction(1, 3)
    b = fractions.Fraction(2, 3)
    c = a / b
    print(a)
    print(b)
    print(c)
