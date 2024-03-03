"""
 * @file   : Student.py
 * @time   : 15:30
 * @date   : 2023/11/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class Student(object):
    # 以下定义的是类型的静态属性
    EnglishName = 'Student'
    ChineseName = '学生'

    def __init__(self, name, age, score):
        # 实例属性通过self关键字定义在 __init__方法中
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        """
        这是一个普通的成员方法
        :return:
        """
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    @staticmethod
    def say_hello():
        print("I can say hi to you!")
    pass

    @classmethod
    def say_hi(cls):
        cls.say_hello()
    pass


