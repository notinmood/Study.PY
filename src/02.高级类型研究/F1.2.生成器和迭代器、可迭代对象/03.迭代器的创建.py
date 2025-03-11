"""
 * @file   : 3.迭代器的创建.py
 * @time   : 8:13
 * @date   : 2024/2/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 方法1和方法2本质是一样的，都是要实现迭代器协议，即实现__next__方法和__iter__方法；
# 只是一个方法是手工创建的，一个方法是使用内建的iter函数自动创建的。
# +--------------------------------------------------------------------------


# 1. 手工创建迭代器
class MyIterator:
    """
    自定义迭代器类
    需要实现__next__方法和__iter__方法
    __next__方法负责返回下一个元素，当没有更多元素时抛出StopIteration异常
    __iter__方法负责返回迭代器本身
    """

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


# 2. 使用列表、元组、集合、字典等可迭代对象配合iter（）方法自动构建迭代器
my_list = [1, 2, 3, 4, 5]
my_list_iterator = iter(my_list)


# 3. 使用生成器函数创建迭代器（生成器是迭代器的一种）
def my_generator():
    """
    通过自定义生成器函数创建迭代器
    :return:
    """
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    my_iterator = MyIterator(my_list)
    for item in my_iterator:
        print(item)
    pass

    print("──分割线───────────────────────────────────")

    for item in my_list_iterator:
        print(item)
    pass

    print("──分割线───────────────────────────────────")

    my_generator = my_generator()
    for item in my_generator:
        print(item)
    pass
