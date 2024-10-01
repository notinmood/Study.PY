"""
 * @file   : index.py
 * @time   : 23:19
 * @date   : 2023/6/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import time
from concurrent.futures import ThreadPoolExecutor
from random import randint


def display(input_value=None):
    """
    普通函数
    :param input_value:
    :return:
    """
    random_value = randint(a=1, b=5)
    time.sleep(random_value)
    content = f"input_value={input_value}, random_value={random_value}"
    print(content)

    pass


if __name__ == '__main__':
    # 2. 多线程执行（在执行结果中可以发现，0-9的结果是随机的）
    with ThreadPoolExecutor() as executor:
        for i in range(10):
            executor.submit(display, input_value=i)

    # # 1. 单线程执行（在执行结果中可以发现，0-9的结果是顺序的）
    # for i in range(10):
    #     display(input_value=i)
pass
