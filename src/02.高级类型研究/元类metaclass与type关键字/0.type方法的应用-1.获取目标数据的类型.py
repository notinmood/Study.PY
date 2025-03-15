"""
 * @file   : 0.type方法的应用.py
 * @time   : 上午8:44
 * @date   : 2024/6/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# | 1.type()方法可以获取对象的类型，包括内置类型和自定义类型。
# | 2.type()方法的返回值是一个类对象，可以用isinstance()方法判断对象是否是某个类型。
# | 3.type()方法的第一个参数可以是对象，也可以是类名，也可以是元类。
#       若是对象实例，则返回对象的类型；
#       若是类型，则返回该类的元类类型；
#       若是元类，则返回该元类的类型（如果是其他自定义元类，则返回自定义元类继承的的类型；如果原类型是type，则返回type）。

# +--------------------------------------------------------------------------
print(type(0))  # <class 'int'>
print(type(int))  # <class 'type'>
print(type("tiger"))  # <class 'str'>
print(type(str))  # <class 'type'>
print(type([1, 2, 3]))  # <class 'list'>
print(type(list))  # <class 'type'>


class User:
    pass


u = User()
print(type(u))  # <class '__main__.User'>
print(type(User))  # <class 'type'>


class MyMeta(type):
    pass


print(type(MyMeta))  # <class 'type'>
print(type(type(type)))  # <class 'type'>    # 元类type本身也是一种类型
