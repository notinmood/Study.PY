"""
 * @file   : 2.开发人员可以通过关键字metaclass为目标类指定特定的元类.py
 * @time   : 上午7:47
 * @date   : 2024/6/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# | 1. 元类是用来创建类的类，它可以控制类的创建过程，并返回一个类对象。
# | 2. 元类可以继承自type，并重写__new__方法，在__new__方法中可以指定创建类的过程。
# | 3. 元类可以为类的创建过程提供更高的灵活性，可以控制类的属性、方法、继承关系等。
# | 4. 元类可以用来创建单例模式、ORM、插件系统等。
# | 5. 元类可以用来实现多继承、多态、插件系统等。
# | 6. 元类可以用来实现面向切面编程（AOP）、插件系统等。
# | 7. 元类可以用来实现插件系统、ORM、单例模式等。
# | 8. 元类可以用来实现缓存、日志、监控、权限控制等。
# | 9. 元类可以用来实现多线程、多进程、协程等。
# | 10. 元类可以用来实现框架、组件化等。
# | 11. 元类可以用来实现插件系统、ORM、单例模式等。
# | 12. 元类可以用来实现缓存、日志、监控、权限控制等。
# | 13. 元类可以用来实现多线程、多进程、协程等。
# +--------------------------------------------------------------------------

class MyMeta(type):

    def __new__(cls, name, bases, attrs):
        print("MyMeta.__new__ called")
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print("MyMeta.__init__ called")
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print("MyMeta.__call__ called")
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    pass


##  输出结果：
# MyMeta.__new__ called
# MyMeta.__init__ called


if __name__ == '__main__':
    my_obj = MyClass()
    ##  输出结果：
    # MyMeta.__call__ called

    print(type(my_obj))
    ##  输出结果：
    # <class '__main__.MyMeta'>
    print(type(MyClass))
    ##  输出结果：
    # <class '__main__.MyMeta'>

    print(type(MyMeta))
    ##  输出结果：
    # <class 'type'>

    print(type(type))
    ##  输出结果：
    # <class 'type'>
