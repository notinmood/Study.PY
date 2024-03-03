"""
 * @file   : person.py
 * @time   : 7:50
 * @date   : 2021/12/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class Person:
    def __init__(self):
        """
        这是一个构造函数
        """
        print('我出生了')

    def __del__(self):
        """
        这是一个析构函数
        :return:
        """
        print('我走了')

    def __enter__(self):
        """

        :return:
        """
        print('__enter__里面')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :return:
        """
        print('__exit__里面')
        self.__del__()

    # noinspection PyMethodMayBeStatic
    def eat(self) -> object:
        """

        :rtype: object
        :return:
        """
        print('吃饭')

    pass

    @staticmethod
    def some_thing():
        print("some thing")
