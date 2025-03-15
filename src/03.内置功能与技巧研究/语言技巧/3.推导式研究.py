"""
 * @file   : 3.推导式研究.py
 * @time   : 16:11
 * @date   : 2022/3/18
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.stringHelper import StringHelper

# +--------------------------------------------------------------------------
# |::::说明::::| Python里面有个很棒的语法糖（syntactic sugar），它就是 list comprehension，
# 有人把它翻译成“列表推导式”，也有人翻译成“列表解析式”。名字听上去很难理解，但是看它的语法就很清晰了。
# 列表推导式（list comprehension）是一种快速生成列表的语法，它以非常简洁的代码实现列表的创建，大体步骤如下：
#  1. 创建或使用一个既已存在的集合（比如range(10)）
#  2. 使用for in 遍历这个集合，每次返回一个元素（比如x）
#  3. 将返回的元素（比如x）或进行处理后的元素（比如x*2）置入一个 [] 列表中，这就形成了 list 推导式。
#
# 虽然名字叫做 list comprehension，但是这个语法同样适用于dict、set等这一系列可迭代（iterable）数据结构。
# 特别注意：元组tuple也可以有生成推导式，但语法与list不同，它需要使用 tuple() 而不是 ()。如果直接使用()，得到的是一个生成器（具体查看“2.使用生成器节省内存.py”）。
# +--------------------------------------------------------------------------

# +--------------------------------------------------------------------------
# |::::说明::::| 各种生成器的语法比较
# ---------------------------------------------------------------------------
#   名称          |           标准写法                                          |  快捷表示
# list 列表推导式  |list(expr(item) for item in iterable)                       |[expr(item) for item in iterable]
# set 集合推导式   |set(expr(item) for item in iterable)                        |{expr(item) for item in iterable}
# dict 字典推导式  |dict(key_expr(item), value_expr(item) for item in iterable) |{key_expr(item):value_expr(item) for item in iterable}
# tuple 元组推导式 |tuple(expr(item) for item in iterable)                      |（没有快捷写法，使用小括号的类似表述，是生成器，生成器调用的是时候才会有结果）
# +--------------------------------------------------------------------------

"""
1. list 列表推导式
"""
my_list = [x ** 2 for x in range(10)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

my_list = [_item * 2 for _item in range(10)]
print(my_list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

my_list = [x * x for x in range(10) if x % 2 == 0]
print(my_list)  # [0, 4, 16, 36, 64]

my_list = [_item for _item in "qingdao city"]
print(my_list)  # ["q", "i", "n", "g", "d", "a", "o", " ", "c", "i", "t", "y"]

my_list = [(x, y) for x in range(5) for y in range(4)]
print(my_list)  # [(0, 0), ..., (4, 2), (4, 3)] 等共包含20个元素

print("使用标准语法的list()函数的列表生成器")
my_list = list(x for x in range(5))
print(my_list)

"""
2. set 集合推导式
"""
chars = {w for w in "Qingdao City"}
print(chars)  # {'o', ..., 'y', 'a'} 因为set的特性，具体的元素顺序每次不一样

chars = {StringHelper.upper_all_chars(_item) for _item in "Beijing City"}
print(chars)  # {'J', 'E', 'C', 'I', ' ', 'G', 'N', 'Y', 'B', 'T'} 因为set的特性，具体的元素顺序每次不一样

print("使用标准语法的set()函数的集合生成器")
chars = set(w for w in "Qingdao City")
print(chars)
"""
3. dict 字典推导式
#  注意：对dict的迭代方式的不同，得到的结果也是不同的。具体参考文件“9.迭代字典的TIP.py” 
"""
my_dict = {"A": "a",
           "B": "b",
           "C": "c"}

my_display = {k: my_dict[k] * 2 for k in my_dict}
print(my_display)
## --output---------------------------
# {'A': 'aa', 'B': 'bb', 'C': 'cc'}

my_display = {_item: my_dict[_item] for _item in my_dict}
print(my_display)
## --output---------------------------
# {'A': 'a', 'B': 'b', 'C': 'c'}

my_display = {k * 2: v * 3 for k, v in my_dict.items()}
print(my_display)
## --output---------------------------
# {'AA': 'aaa', 'BB': 'bbb', 'CC': 'ccc'}

# 可以加入过滤条件
my_display = {k * 2: v * 3 for k, v in my_dict.items() if k == "A"}
print(my_display)
## --output---------------------------
# {'AA': 'aaa'}

print("使用标准语法的dict()函数的集合生成器")
my_display = dict((k, my_dict[k]) for k in my_dict)
print(my_display)
"""
4. 元组推导式
"""
print("──以下是元组推导式───────────────────────────────────")
# 由于推导式使用()、[] {}这种快捷表示方式中的()被生成器占用，因此原则推导式只能使用标准的函数tuple()构建
my_tuple = tuple(x ** 2 for x in range(10))
print(my_tuple)

# 但如果不使用tuple()，而是使用()，得到的结果是则是一个生成器对象
my_generator = (x ** 2 for x in range(10))
print(my_generator)
# 生成器对象，则需要使用next()函数或者使用for...in，才能得到具体的值
print(next(my_generator))

for _item in my_generator:
    print(_item)
pass
