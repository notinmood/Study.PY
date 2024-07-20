"""
 * @file   : 1.排序算法测试.py
 * @time   : 下午4:24
 * @date   : 2024/4/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

# 请写一个冒泡排序的测试程序，并测试其运行时间。

import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            pass
        pass

    return arr


if __name__ == '__main__':
    _arr = [random.randint(0, 100) for _ in range(10000)]
    start_time = time.time()
    bubble_sort(_arr)
    end_time = time.time()
    print(f"Bubble sort running time: {end_time - start_time} seconds")
