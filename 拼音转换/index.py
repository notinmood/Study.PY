"""
 * @file   : index.py
 * @time   : 下午4:08
 * @date   : 2024/5/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from xpinyin import Pinyin

if __name__ == '__main__':
    p = Pinyin()
    print(p.get_pinyin('你好，世界！', splitter=' ', tone_marks='marks'))
