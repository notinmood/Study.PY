"""
 * @file   : www.py
 * @time   : 20:35
 * @date   : 2022/3/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from itertools import product
# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 嵌套循环。在一个循环体中嵌套另一个循环体。这就是笛卡尔积方式，使用product()函数可以实现这样的嵌套循环。
# +--------------------------------------------------------------------------

if __name__ == '__main__':
    list1 = range(1, 4)
    list2 = range(4, 7)
    list3 = range(7, 10)

    # 1. 普通地嵌套循环
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                print(f"{item1}*{item2}*{item3}={item1 * item2 * item3}")
                print(f"{item1}+{item2}+{item3}={item1 + item2 + item3}")
            pass
        pass
    pass

    print("=" * 50)

    # 2. 使用itertools.product()函数实现嵌套循环
    for i, j, k in product(list1, list2, list3):
        print(f"{i}*{j}*{k}={i * j * k}")
        print(f"{i}+{j}+{k}={i + j + k}")
    pass
