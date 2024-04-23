"""
 * @file   : student.py
 * @time   : 8:02
 * @date   : 2023/12/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class Student(object):
    def __init__(self, name, age, grade, sex="male", score=60):
        self.name = name
        self.age = age
        self.grade = grade
        self.sex = sex
        self.score = score

    def __str__(self):
        return "Student object (name: %s, age: %d, grade: %d)" % (self.name, self.age, self.grade)

    def __del__(self):
        print("Student object is destroyed!")

    def __len__(self):
        return self.grade

    def __getitem__(self, item):
        if item == 0:
            return self.name
        pass


pass
