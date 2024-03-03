"""
 * @file   : 10.使用enumerate在loop中快速获取索引信息.py
 * @time   : 15:06
 * @date   : 2024/2/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# enumerate() 是一个 Python 内置函数，用于将一个可遍历的数据对象(如列表、元组或字符串)
# 组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# +--------------------------------------------------------------------------

if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5]

    for index, item in enumerate(number_list):
        print(f"index: {index}, item: {item}")
    pass

    print("──分割线───────────────────────────────────")

    # 索引号默认以 0 开始，如果需要从 1 开始，可以使用 start 参数指定起始索引号。
    for index, item in enumerate(number_list, start=1):
        print(f"index: {index}, item: {item}")
    pass
pass
