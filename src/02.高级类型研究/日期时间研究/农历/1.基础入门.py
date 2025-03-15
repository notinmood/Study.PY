"""
 * @file   : 1.ABC.py
 * @time   : 19:02
 * @date   : 2025/2/3
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from datetime import datetime

from zhdate import ZhDate

if __name__ == '__main__':
    # 农历日期对象
    date1 = ZhDate(2022, 2, 2)  # 新建农历 2022年二月初二（龙抬头）的日期对象
    print(date1)  # 农历2022年2月2日

    # 从阳历日期转换成农历日期对象
    dt_date2 = datetime(2022, 2, 6)
    date2 = ZhDate.from_datetime(dt_date2)
    print(date2)  # 农历2022年2月6日

    # 农历日期对象转为阳历日期对象
    dt_date3 = date2.to_datetime()
    print(dt_date3)  # 2022-02-06 00:00:00

    date3 = ZhDate(2020, 4, 15)  # 新建农历 2020年4月15日
    print(date3)  # 农历2020年4月15日
    print(date3.to_datetime())  # 2020-05-07 00:00:00

    data4= datetime(2025, 1, 29)
    date4 = ZhDate.from_datetime(data4)
    print(date4.chinese())  # 二零二五年正月初一 乙巳年 (蛇年)
