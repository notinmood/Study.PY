"""
 * @file   : 5.dataclass使用.py
 * @time   : 17:24
 * @date   : 2023/12/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass, field

"""
▌参考资料：https://blog.csdn.net/xq151750111/article/details/127072870?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-127072870-blog-119545119.235^v39^pc_relevant_3m_sort_dl_base2&spm=1001.2101.3001.4242.1&utm_relevant_index=3
"""


# 使用@dataclass定义的数据类
@dataclass
class Person(object):
    # 这种定义方式实际上是为类型定义了静态属性，
    # 然后装饰器@dataclass自动对其进行了“二次加工”，使其成为了对象的实例属性
    name: str
    grade: str
    age: int = field(default=18)


pass


# 普通类型
class Animal(object):
    name: str = '小动物'
    age: int


pass

if __name__ == '__main__':
    p = Person('ShanDong', 'A', 23)  # 定义方法A
    p = Person(name='ShanDong', grade='A', age=23)  # 定义方法B
    print(p)
    print(p.name)
    print(p.age)
    print(p.grade)
    print(p.name, p.age, p.grade)

    print("──分割线───────────────────────────────────")

    # # 以下代码无法使用，因为在定义的时候没有为类型的静态属性进行初始化
    # print(Person.name)
    # # 但以下age属性就能访问，因为在定义age的时候经过了初始化处理了
    print(Person.age)

    print(Animal.name)
    # # 如果在定义的时候没有初始化，则不能访问
    # print(Animal.age)
