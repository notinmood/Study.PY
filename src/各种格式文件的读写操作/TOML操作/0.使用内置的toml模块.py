"""
 * @file   : 0.使用内置的toml模块.py
 * @time   : 7:09
 * @date   : 2024/3/30
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import tomllib

if __name__ == '__main__':
    # here = os.path.abspath(os.path.dirname(__file__))
    # toml_file = os.path.join(here, r"_res\my.toml")
    toml_file = r"_res\my.toml"
    with open(toml_file, "rb") as _file:
        toml = tomllib.load(_file)
    print(toml)
    pass
