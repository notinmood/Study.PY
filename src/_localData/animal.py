"""
 * @file   : animal.py
 * @time   : 上午9:09
 * @date   : 2024/6/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def eat(self):
        print(f"{self.__class__} is eating.")

    # @abstractmethod
    # def take_baby(self):
    #     return a: Animal
