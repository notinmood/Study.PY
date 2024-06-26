"""
 * @file   : 01.迭代器入门.py
 * @time   : 10:48
 * @date   : 2024/2/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# 1. 可以被next()函数不断返回下一个值的对象称为迭代器：Iterator
# 2. 使用iter()函数将可迭代的对象（如list、dict等）转化成迭代器Iterator

def convert_iterable_to_iterator():
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)
    print(next(my_iter))  # 1
    print(next(my_iter))  # 2
    print(next(my_iter))  # 3
    print(next(my_iter))  # 4
    print(next(my_iter))  # 5


if __name__ == '__main__':
    # 调用函数
    convert_iterable_to_iterator()
