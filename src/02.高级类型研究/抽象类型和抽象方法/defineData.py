"""
 * @file   : 1.定义抽象类型.py
 * @time   : 下午6:05
 * @date   : 2024/4/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from abc import ABCMeta, ABC, abstractmethod


class Shape(ABC):
    ...


class City(metaclass=ABCMeta):
    ...


class Country(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        print("This is a Country.")


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


class Bird(Animal):
    def sound(self):
        print("Tweet!")
