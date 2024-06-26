"""
 * @file   : versionHelper.py
 * @time   : 16:46
 * @date   : 2024/3/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import re


class VersionHelper(object):
    """
    版本号处理工具类
    本类型处理公认标准的三段式版本号“X.Y.Z”,其中：
        X为主版本号（Major）；
        Y为次版本号（Minor）；
        X为修正版本号（patch）
    """

    @staticmethod
    def get_digits(original_version: str):
        """
        获取版本号中的数字部分
        """
        version_match = re.search(r"(\d+\.\d+\.\d+)", original_version)

        current_version = version_match.group(1)
        return current_version

    pass

    @classmethod
    def increase_patch(cls, original_version: str):
        """
        给版本号中的修正版本号加1
        param:original_version: 原始版本号，形如“1.2.3”
        """
        old_sub_string = cls.get_digits(original_version)
        digit_list = list(map(int, old_sub_string.split(".")))
        digit_list[-1] += 1

        string_list = list(map(str, digit_list))
        new_sub_string = ".".join(string_list)

        return original_version.replace(old_sub_string, new_sub_string)

    pass


pass
