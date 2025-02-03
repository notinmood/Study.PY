"""
 * @file   : StudentClass.py
 * @time   : 18:43
 * @date   : 2021/12/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.stringHelper import StringHelper


class StudentClass(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return StringHelper.format("班级名称为:{0}", self.name)

    def display(self):
        return self.__str__()
