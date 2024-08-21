"""
 * @file   : 高精度除法.py
 * @time   : 下午7:32
 * @date   : 2024/8/21
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import decimal

# 常规除法
print(10 / 3)  # 3.3333333333333335

# 高精度除法
a = decimal.Decimal('10.0')
b = decimal.Decimal('3.0')
c = a / b
print(c)  # 3.333333333333333333333333333

# 精度控制
c = a / b
print(c.quantize(decimal.Decimal('0.01')))  # 3.33
