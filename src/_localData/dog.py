"""
 * @file   : dog.py
 * @time   : 上午9:13
 * @date   : 2024/6/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from .animal import Animal


class Dog(Animal):
    def eat(self):
        super().eat(self)

    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f"{self.name} is barking!")
