
"""
调用第三方库
"""
from BasicLibrary.data.stringHelper import StringHelper

if __name__ == '__main__':
    x = 10
    y = 20

    # 要么都写数字索引，要么都不写；不能有的写有的不写
    print("x,y的值为{},{}".format(x, y))
    print("x,y的值为{0},{1}".format(x, y))
    print(str.format("x,y的值为{},{}", x, y))

    name = "小明"
    height = 175

    print("────────────────────────PY系统的缺省方法────────────────────────")
    print(f"{name}的身高是{height}cm")

    print("────────────────────────使用 DIY方法1────────────────────────")
    whole = StringHelper.format("{name}的身高是{height}", name=name, height=height)
    print(whole)

    print("────────────────────────使用 DIY方法2────────────────────────")
    whole = StringHelper.format("{0}的身高是{1}", name, height)
    print(whole)
