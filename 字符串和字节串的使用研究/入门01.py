"""
 * @file   : t.py
 * @time   : 15:26
 * @date   : 2024/1/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
if __name__ == '__main__':
    a_en = 'HelloWord'
    print(a_en)  # 'HelloWord'

    b_en_8 = a_en.encode(encoding='utf-8')
    print(b_en_8)  # b"HelloWord"

    b_en_16 = a_en.encode(encoding='utf-16')
    print(b_en_16)  # b"\xff\xfeH\x00e\x00l\x00l\x00o\x00W\x00o\x00r\x00d\x00"

    b_en_32 = a_en.encode(encoding='utf-32')
    print(b_en_32)
    ## --output---------------------------
    # 输出的内容信息
    # b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00W\x00\x00\x00o\x00\x00\x00r\x00\x00\x00d\x00\x00\x00'

    a_cn = "你好"
    b_cn_8 = a_cn.encode(encoding='utf-8')
    print(b_cn_8)  # b"\xe4\xbd\xa0\xe5\xa5\xbd"

    # ...:
    # b
    # Out[5]: b'helloWord'
    # print(type(b)) # <class 'bytes'>
