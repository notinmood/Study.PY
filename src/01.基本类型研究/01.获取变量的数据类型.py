"""
 * @file   : 01.获取变量的数据类型.py
 * @time   : 15:39
 * @date   : 2025/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: Less is more.Simple is best!
"""
# 1.定义变量并赋值
age: int = 25
name: str = "ShanDong"

# 2.1获取变量的数据类型
print(type(age))  # 输出：<class 'int'>
print(type(name))  # 输出：<class 'str'>

# 2.2使用type函数获取变量的数据类型
print(type(age) == int)  # 输出：True
print(type(name) == str)  # 输出：True

# 2.3 使用isinstance函数判断变量的数据类型
print(isinstance(age, int))  # 输出：True
print(isinstance(name, str))  # 输出：True

# 3.type函数可以获取变量的类型，返回值是type类型。
print(type(type(123)))  # 输出：<class 'type'>
