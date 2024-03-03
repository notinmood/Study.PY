"""
 * @file   : TypedDict使用.py
 * @time   : 9:13
 * @date   : 2023/12/4
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from typing import TypedDict


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 1. 通过TypedDict创建的强类型字典对象的属性，依然需要通过 xx.["yy"] 的形式访问
# 2. 强类型字典对象，只能存储指定的属性名称，其他未定义的属性名称，无法存储
# 2. 强类型字典对象，只能存储指定的数据类型，其他的数据类型，无法存储
# +--------------------------------------------------------------------------

class MyUser(TypedDict):
    name: str
    age: int
    sex: str


if __name__ == '__main__':
    print("──以下是普通字典的信息───────────────────────────────────")
    # 1. 普通的字典（dict）
    common_dict = {'name': 'ShanDong', 'age': 25, 'sex': 'male'}
    print(common_dict)
    # 使用字典内key的时候，必选通过字符串的形式引用
    print(common_dict['name'])

    print("──以下是强类型字典的信息───────────────────────────────────")

    # 2. 强类型字典（TypedDict）
    User = TypedDict('User', {"name": str, "age": int, "sex": str})
    print(User)

    # 使用强类型字典创建完成类型的时候，可以直接使用key引用，不需要字符串形式。
    # -> 但是这些属性是类型上的属性，不是对象实例上的属性。对象实例上的属性，要使用[""]的方式访问
    User.name = 'shandong'
    User.age = 25
    User.sex = 'male'

    print(User.name)
    print(User.age)

    print("──mm───────────────────────────────────")
    # 以下代码会在静态检测的时候，出现警告（sex2为定义，是“意外实参”；并且没有必选的属性sex）；但运行时不会出错。
    mm = User(name='shandong', age=25, sex2='male')
    print(mm)

    # 以下代码会在静态检测的时候，出现警告（）；但运行时不会出错。
    ww = User()
    print(ww)

    print("──分割线───────────────────────────────────")
    lisi: User = {'name': 'lisi', 'age': 25, 'sex': 'male'}
    print(lisi)

    # print(lisi.name)
    print("──分割线───────────────────────────────────")
    print(MyUser)
    # 以下代码会在静态检测的时候，出现警告；但运行时不会出错。
    wangwu: MyUser = {'name': 'wangwu', 'age': 25, 'sex4': 'male'}
    print(wangwu)

    # print(MyUser.name)
    print("──分割线───────────────────────────────────")
    zhao = MyUser(**{"name": "zhaoliu", "age": 25, "sex": "male"})

    print(zhao)

    # # 以下代码会在运行时报错。因为 TypedDict 创建的不是强类型对象，不具有命名属性
    # print(zhao.name)
    # print(zhao.age)

    # 通过TypedDict创建的强类型字典对象的属性，依然需要通过 xx.["yy"] 的形式访问
    print("zhao的name为：" + zhao["name"])

    pass
