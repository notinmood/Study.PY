"""
 * @file   : using.with方式调用.py
 * @time   : 17:37
 * @date   : 2023/7/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from 构造函数与析构函数.person import Person

with Person() as person:
    person.eat()
pass

print("══════════════════════════")
print("程序结束")

"""
在以下输出结果中：
1. 出现了"__enter__"和"__exit__"的输出，这是因为 with...as结构自动调用的结果。
2. 出现了"我出生了"是类型初始化的结果，即在创建person对象时自动调用的结果。
3. 出现了"吃饭"的输出，这是因为person对象调用了eat方法的结果。
4. 出现了"我走了"的输出，这是因为“__exit__”方法内手工调用“__del__”的结果，如果不是手工调用，类型实例的销毁方法不会主动执行。
"""

## --output---------------------------
# 我出生了
# __enter__里面
# 吃饭
# __exit__里面
# 我走了


