"""
 * @file   : 各种集合类型的创建与使用.py
 * @time   : 18:13
 * @date   : 2023/7/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
# 1. 用构造函数生成集合对象
my_dict = dict()
my_set = set()
my_list = list()
my_tuple = tuple()

# 2. 用快捷方式生成集合对象
my_dict = {}
my_list = []
my_tuple = ()

# 3. 向集合添加元素
my_set.add(1)
my_set.add(2)

my_list.append(1)
my_list.insert(0, 1)

my_dict[1] = 1
my_dict[2] = 2

# tuple 只能在初始化的时候构建，构建完成就不可以再次修改，因此其没有add，insert等方法
my_tuple = (1, 2)

print(my_tuple)
# 以下方法不存在
# my_tuple.add(1)

my_dict["a"] = "a"
my_dict[0] = "33"
my_dict["wps"] = "金山"
my_dict["office"] = "微软"

# 新版的Python对dict进行了改进，他内部是有序的：各个item按照置入的顺序前后排列
print(my_dict)
## --output---------------------------
# {1: 1, 2: 2, 'a': 'a', 0: '33', 'wps': '金山', 'office': '微软'}
