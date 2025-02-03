"""
 * @file   : 3.namedtuple使用.py
 * @time   : 7:52
 * @date   : 2023/12/5
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from collections import namedtuple

if __name__ == '__main__':
    Player = namedtuple('Player', ['name', 'number', 'position', 'age', 'grade'])
    xiedali = Player('ShanDong Xiedali', 9727005, 'GK', 25, 80)
    print(xiedali.age)
    print(xiedali.name)
    print(xiedali.number)
    print(xiedali.position)
    print(xiedali.grade)
    print(xiedali)

    # # 以下代码会报错，因为tuple是只读的，不能修改属性
    # xiedali.age = 26
