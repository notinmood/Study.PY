"""
 * @file   : 2.reduce的使用.py
 * @time   : 10:09
 * @date   : 2024/1/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from functools import reduce

if __name__ == '__main__':
    result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    print(result)
    # --output---
    # 15
