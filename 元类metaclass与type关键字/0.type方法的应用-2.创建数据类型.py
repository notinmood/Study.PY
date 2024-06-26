"""
 * @file   : 0.type方法的应用.py
 * @time   : 上午8:44
 * @date   : 2024/6/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 语法：
# type(类名，由父类名称组成的元组（可以为空，为空则默认继承object），包含属性的字典（名称和值）)

# +--------------------------------------------------------------------------
def show(self):
    print(f"{self.age}")
    print("展示自己")


Person = type("Person", (object,), {"age": 18, "name": "jkc", "show": show})

if __name__ == '__main__':
    p = Person()
    print(p.age)
    print(p.name)
    p.show()
