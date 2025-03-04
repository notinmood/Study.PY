"""
 * @file   : index.py
 * @time   : 11:29
 * @date   : 2023/7/19
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from pywencai import get


if __name__ == '__main__':
    res = get(query='人气排行榜前10名；涨停；行业', loop=True)
    print(res)
pass
