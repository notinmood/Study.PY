"""
 * @file   : 2.开发人员可以通过关键字metaclass为目标类指定特定的元类.py
 * @time   : 上午7:47
 * @date   : 2024/6/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from abc import abstractmethod, ABCMeta


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 示例演示：
# ABCMeta是Python中的抽象基类元类，它可以用来创建抽象基类，并提供抽象方法的实现。
# +--------------------------------------------------------------------------
class MyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        ...


pass

if __name__ == '__main__':
    ...
    # # 以下代码将会报错，因为MyAnimal类是抽象类，不能实例化
    # # 实例化MyAnimal类，并调用eat方法
    # my_animal = MyAnimal()
    # my_animal.eat()
