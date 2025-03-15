"""
 * @file   : 入门03.u型字符串和u型字节串.py
 * @time   : 16:24
 * @date   : 2024/1/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
if __name__ == '__main__':
    input_a = "北京市"
    output_a = input_a.encode("unicode_escape")
    print(output_a)  # b"\\u5317\\u4eac\\u5e02"

    # 1. Python中，遇到\u型字符串，其自动会将转换为Unicode字符。
    a = '\u5317\u4eac\u5e02'
    print(a)  # 北京市

    # 2. 但如果\u型“字符串”前面加了b，那就不是字符串而是字节类型了，需要decode()函数转换。
    a = b"\\u5317\\u4eac\\u5e02"  # 其中第一个\是转义字符，是让第二个\原义使用
    a = a.decode('unicode_escape')
    print(a)  # 北京市

