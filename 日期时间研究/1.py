"""
 * @file   : 1.py
 * @time   : 12:14
 * @date   : 2024/3/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import time
from datetime import datetime


def generate_16_digit_timestamp():
    # 获取当前时间的微秒级时间戳
    timestamp_micro = datetime.now().timestamp() * 1_000_000
    # 将时间戳转换为整数
    timestamp_micro_int = int(timestamp_micro)
    # 确保时间戳是16位的，这可能需要根据你的具体需求调整
    return str(timestamp_micro_int)[:16]


if __name__ == '__main__':
    print("──当前时间───────────────────────────────────")
    print(datetime.now())

    print("──获取时间戳的两种方式───────────────────────────────────")
    print(time.time())
    print(datetime.now().timestamp())

    print("──生成16位时间戳────────────────────────────────────────────")
    print(generate_16_digit_timestamp())
