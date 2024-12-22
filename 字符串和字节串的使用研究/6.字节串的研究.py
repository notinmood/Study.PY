"""
 * @file   : 6.字节串的研究.py
 * @time   : 0:33
 * @date   : 2024/1/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

if __name__ == '__main__':
    # 1. 字节串的定义
    my_bytes = b"abcd"
    # 以下是为了消除ide参数的警告而做的PolyFill
    # noinspection all
    print(my_bytes)  # b'abcd'
    print(my_bytes[0])  # 97
    # 以下是为了消除ide的警告而做的PolyFill
    # noinspection all
    print(my_bytes[2:3])  # b'c'
    print(my_bytes[-1])  # 100

    # # b包含的字符串称为字节串，但其内部仅支持ASCII字符，不能直接包含中文
    # # 以下代码会出现错误：“SyntaxError: bytes can only contain ASCII literal characters”
    # my_byte_string = b"我是一个中国人！"
    # print(my_byte_string)

    # 2. 字节串和字节串的编码解码转换
    s = "中文"
    b = s.encode()  # 默认使用utf-8
    print(b)  # b'\xe4\xb8\xad\xe6\x96\x87'

    s = "中文"
    b = s.encode(encoding="gbk")  # 明确使用GBK编码规则
    print(b)  # b'\xd6\xd0\xce\xc4'

    my_bytes = b"\xe4\xb8\xad\xe6\x96\x87"
    my_string = my_bytes.decode()  # 默认使用utf-8
    print(my_string)  # 中文

    my_bytes = b'\xd6\xd0\xce\xc4'
    my_string = my_bytes.decode(encoding="gb2312")  # gb2312是GBK的一个子集，是可以对GBK编码的bytes进行解码的
    print(my_string)  # 中文
