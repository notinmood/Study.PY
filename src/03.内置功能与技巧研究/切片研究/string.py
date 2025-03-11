"""
 * @file   : string.py
 * @time   : 15:30
 * @date   : 2021/12/4
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from pprint import pprint


def operate1():
    my_str = '0123456789'
    print(my_str[0:3])  # 截取第一位到第三位的字符
    print(my_str[:])  # 截取字符串的全部字符
    print(my_str[6:])  # 截取第七个字符到结尾
    print(my_str[:-3])  # 截取从头开始到倒数第三个字符之前
    print(my_str[2])  # 截取第三个字符
    print(my_str[-1])  # 截取倒数第一个字符
    print(my_str[::-1])  # 创造一个与原字符串顺序相反的字符串

    pprint('截取倒数第三位与倒数第一位之前的字符')
    print(my_str[-3:-1])  # 截取倒数第三位与倒数第一位之前的字符
    print(my_str[-3:])  # 截取倒数第三位到结尾
    print("逆序截取")
    print(my_str[:-5:-3])  # 逆序截取，具体啥意思没搞明白？


pass


def operate2():
    my_data = "i love China!"
    """
    通过[:]取切片的时候，他是一个前闭后开的区间。
    """
    # 取到倒数第一个，但不包含倒数第一个
    print(my_data[:-1])
    # 如果要要取到最后一个，那么冒号后就不写任何内容
    print(my_data[:])
    # 不取第0个
    print(my_data[1:])
    # 倒叙取得数据
    print(my_data[::-1])


if __name__ == '__main__':
    operate1()
    operate2()
pass
