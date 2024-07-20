"""
 * @file   : 15.海象运算符.py
 * @time   : 下午3:37
 * @date   : 2024/7/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
# 如果一个变量被赋值后立即被使用，那么就可以使用海象运算符

numbers = [1, 2, 3, 4, 5]
if (x := len(numbers)) >= 5:
    print(f"✅ 多于5个元素的数组，当前有{x}个元素")
else:
    print(f"❌ 少于5个元素的数组，当前有{x}个元素")
