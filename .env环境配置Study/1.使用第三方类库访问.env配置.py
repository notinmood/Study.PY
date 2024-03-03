"""
 * @file   : index.py
 * @time   : 10:14
 * @date   : 2021/12/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import dotenv

"""
使用 python-dotenv 模塊，讀取.env環境配置.
使用之前，請先安裝 python-dotenv 模塊
"""

if __name__ == '__main__':
    result = dotenv.dotenv_values()
    print(result)
    if result:
        print(result["ROOT_URL"])
        # print(result["aaa"])
    pass


