"""
 * @file   : 0.定义抽象类的两种方式.py
 * @time   : 下午8:23
 * @date   : 2024/6/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from abc import ABC, ABCMeta, abstractmethod


# 定义抽象类的方式1
class MyAbstractClass1(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass


# 定义抽象类的方式2
class MyAbstractClass2(metaclass=ABCMeta):
    @abstractmethod
    def my_abstract_method(self):
        pass
