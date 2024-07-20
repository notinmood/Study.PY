"""
 * @file   : person.py
 * @time   : 7:50
 * @date   : 2021/12/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class Person:
    def __new__(cls, *args, **kwargs):
        """
        这是一个重写的__new__方法，用来控制对象的创建
        :param cls:
        :param args:
        :param kwargs:
        :return:
        """
        print('__new__里面，我出生了！')
        return object.__new__(cls)  # new方法必须返回一个实例对象

    def __init__(self):
        """
        这是一个初始化方法，用来初始化对象
        """
        print('__init__里面，我可以打扮的漂漂亮亮！')

    def __del__(self):
        """
        这是一个析构函数
        :return:
        """
        print('__del__里面，我死掉了！')

    def __enter__(self):
        """

        :return:
        """
        print('__enter__里面，我准备好了！')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :return:
        """
        print('__exit__里面，我的事务处理完了！')
        # self.__del__() # 不用手动调用析构函数，因为__exit__会被系统自动调用

    # noinspection PyMethodMayBeStatic
    def eat(self) -> None:
        """

        :rtype: object
        :return:
        """
        print('》》》我正在吃饭ing！')

    pass

    @staticmethod
    def do_something():
        print("》》》Do something！")
