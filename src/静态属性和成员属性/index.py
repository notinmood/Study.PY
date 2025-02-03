"""
 * @file   : index.py
 * @time   : 15:56
 * @date   : 2023/11/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from 静态属性和成员属性.student import Student

if __name__ == '__main__':
    s = Student('ShanDong', 18, 80)

    # 1. 在对象实例上调用对象成员
    # 1.1 调用成员属性
    print("1.1 调用成员属性:")
    print(s.name)

    # 1.2 调用成员方法
    print("# 1.2 调用成员方法:")
    grade = s.get_grade()
    print(grade)

    # 1.3 在对象实例上调用静态属性
    s.ChineseName = "中国名字"
    print(s.ChineseName)

    print("──分割线───────────────────────────────────")

    # 2. 在类型上调用类型成员
    # 2.1 调用静态属性
    print("# 2.1 调用静态属性:")
    cn = Student.ChineseName
    print(cn)

    # 2.2 调用静态方法
    print("# 2.2 调用静态方法:")
    Student.say_hello()
