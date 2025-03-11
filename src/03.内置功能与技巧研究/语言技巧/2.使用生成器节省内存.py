"""
 * @file   : 2.使用生成器节省内存.py
 * @time   : 7:13
 * @date   : 2022/3/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import sys

"""
1. 列表生成式与生成器具有相同的语法，不同点在于列表生成式使用的是中括号、集合生成器字典生成器使用的是大括号，而生成器使用的是小括号。
2. 生成器通过类似于懒加载的方式计算我们需要的元素，因此它一次只生成一个元素，并且只在需要的时候才生成。
即，生成器节省内容的原理是：
构建生成器到时候，并不为其立即赋值(list等数据类型是立即赋值的)；只有当调用到时候，才赋值和返回当前值。
3. 小括号本身是元组的表述字符，但此处小括号被用作生成器，所以如果要使用元组推导式就需要加入关键字tuple和小括号，即tuple()。
"""
my_list = [i for i in range(100)]  # list 列表推导式
my_tuple = tuple(i for i in range(100))  # tuple元组推导式
my_gen = (i for i in range(100))  # 生成器表达式

print(sys.getsizeof(my_list), 'bytes')  # 920 bytes
print(sys.getsizeof(my_tuple), 'bytes')  # 840 bytes
print(sys.getsizeof(my_gen), 'bytes')  # 192 bytes

print("my_list: ", my_list)
print("my_tuple: ", my_tuple)
print("my_gen: ", my_gen)

# +--------------------------------------------------------------------------
# |::说明·| 上面的 my_gen 里面并没有真实的数据；下面调用代码的时候，才会赋值和使用值。
# +--------------------------------------------------------------------------
print("my_gen内具体的数据为：")
for key in my_gen:
    print(key)
pass
