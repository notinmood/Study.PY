"""
 * @file   : 0.使用.py
 * @time   : 8:06
 * @date   : 2023/12/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from _res.student import Student

if __name__ == '__main__':
    s = Student("zhangsan", 18, 99)
    print("以下是类型的打印信息：")
    print(Student)
    print("以下是对象实例的打印信息：")
    print(s)

    print("以下是对象实例的属性信息：")
    print(s.name)
    print(s.age)

    # 普通类型的实例属性无法通过静态方式获取
    # 以下代码会报错
    # print(Student.age)

    print("──这是一个分割线───────────────────────────────────")
    # print(Student.age)
