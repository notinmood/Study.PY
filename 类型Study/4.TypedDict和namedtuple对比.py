"""
 * @file   : 4.TypedDict和namedtuple对比.py
 * @time   : 7:44
 * @date   : 2023/12/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from collections import namedtuple
from typing import TypedDict

"""

"""

if __name__ == '__main__':
    # 1.  TypedDict字典类型
    User = TypedDict('User', {"name": str, "age": int, "sex": str})
    # 使用快捷方式创建字典后，获得类型
    print(User)

    myUser = User(name='shandong', age=25, sex='male')
    print(myUser)
    print(myUser['name'])
    print(myUser['age'])

    # # 使用强类型字典的时候，可以直接使用key引用，不需要字符串形式
    # User.name = 'shandong'
    # # User.age = 25
    # # User.sex = 'male'
    #
    # print(User.name)
    # print(User.age)

    print("──分割线───────────────────────────────────")

    # 2. namedtuple命名元组类型
    Player = namedtuple('Player', ['name', 'no', 'position', 'age', 'grade'])
    print("namedtuple的类型信息为：")
    print(Player)

    # 2.1 创建类型之后，类型上就有了静态的属性，可以通过类型直接调用
    print(Player.name)

    # 2.2 通过类型再创建对象实例
    player1 = Player('ShanDong Xiedali', 9727005, 'GK', 25, 80)

    print("player的实例信息为：")
    print(player1)
    print(player1.age)
    print(player1.name)
    print(player1.no)
    print(player1.position)
    print(player1.grade)

    # 2.3 在类型上设置的静态属性值，会影响实例上的属性值
    Player.name = "the player"
    player2 = Player('china boy', 123, 'MF', 20, 77)
    print(player2)

    print("在类型上设置的属性值，会影响实例上的值:")
    print(player2.name)  # 此处输出 "the player"，而不是 "china boy"
