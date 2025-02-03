"""
 * @file   : 2.使用BasicLibrary.Python访问.env配置.py
 * @time   : 21:37
 * @date   : 2022/3/5
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.configHelper import ConfigHelper

if __name__ == '__main__':
    s = ConfigHelper.get_item("", "ROOT_URL")
    print(s)
