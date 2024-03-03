"""
 * @file   : returnResult.py
 * @time   : 18:42
 * @date   : 2024/1/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass


@dataclass
class ReturnResult[T](object):
    """
    返回结果
    """
    status: bool = True
    message: str = ""
    data: T = None
