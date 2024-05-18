"""
 * @file   : 1.拉平多层嵌套的ifelse.py
 * @time   : 下午10:01
 * @date   : 2024/4/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from _res.student import Student


def multi_nested_clause1(student: Student) -> Student | None:
    # 【BAD】使用and连接多个条件
    if student.sex == "female" and student.age < 25 and student.score >= 60:
        return student  # 各种条件都满足，返回学生信息
    else:
        return None  # 条件不满足，返回None
    pass


def multi_nested_clause2(student: Student) -> Student | None:
    # 【BAD】使用条件多次嵌套进行判定
    if student.sex == "female":
        if student.age < 25:
            if student.score >= 60:
                return student  # 各种条件都满足，返回学生信息
            else:
                return None  # 条件2不满足，返回None
            pass
        else:
            return None  # 条件1不满足，返回None
        pass
    else:
        return None  # 条件0不满足，返回None
    pass


def flatten_clause1(student: Student) -> Student | None:
    # 【OK】对于简单条件，可以将不满足条件的逻辑提前返回来实现拉平效果

    if student.sex != "female":  # 条件1
        return None  # 退出函数
    pass

    if student.age > 25:  # 条件2
        return None  # 退出函数
    pass

    if student.score < 60:  # 条件3
        return None  # 退出函数
    pass

    # 以上条件都不满足，执行以下语句
    return student  # 返回结果


def flatten_clause2(student: Student) -> Student | None:
    # 【OK】如果是复杂的判定，可以用有提前退出的while循环来实现拉平效果
    result = None  # 结果信息
    flag = True  # 标记是否满足条件
    while flag:  # 无限循环，直到满足条件退出
        if student.sex != "female":  # 条件1
            break  # 退出循环
        pass

        if student.age > 25:  # 条件2
            break  # 退出循环
        pass

        if student.score < 60:  # 条件3
            break  # 退出循环
        pass

        # 以上条件都不满足，执行以下语句
        result = student  # 结果列表添加元素
        flag = False  # 退出循环
    pass

    return result  # 返回结果


if __name__ == '__main__':
    _student = Student("Tom", 26, 3, "male", 68)
    _result = flatten_clause1(_student)
    print(_result)  # 输出结果：None

    _student = Student("Jane", 24, 3, "female", 70)
    print(flatten_clause2(_student))  # 输出结果：Jane
