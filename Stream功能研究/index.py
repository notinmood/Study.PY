"""
 * @file   : index.py
 * @time   : 上午9:36
 * @date   : 2024/5/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from pprint import pprint

from superstream import Stream

students = [
    {"id": 20160001, "name": "孔明", "age": 20, "grade": 1, "major": "土木工程", "school": "武汉大学"},
    {"id": 20160002, "name": "伯约", "age": 21, "grade": 2, "major": "信息安全", "school": "武汉大学"},
    {"id": 20160003, "name": "玄德", "age": 22, "grade": 3, "major": "经济管理", "school": "武汉大学"},
    {"id": 20160004, "name": "云长", "age": 21, "grade": 2, "major": "信息安全", "school": "武汉大学"},
    {"id": 20161001, "name": "翼德", "age": 21, "grade": 2, "major": "机械与自动化", "school": "华中科技大学"},
    {"id": 20161002, "name": "元直", "age": 23, "grade": 4, "major": "土木工程", "school": "华中科技大学"},
    {"id": 20161003, "name": "奉孝", "age": 23, "grade": 4, "major": "计算机科学", "school": "华中科技大学"},
    {"id": 20162001, "name": "仲谋", "age": 22, "grade": 3, "major": "土木工程", "school": "浙江大学"},
    {"id": 20162002, "name": "鲁肃", "age": 23, "grade": 4, "major": "计算机科学", "school": "浙江大学"},
    {"id": 20163001, "name": "丁奉", "age": 24, "grade": 5, "major": "土木工程", "school": "南京大学"}
]


def filter_by_school():
    whu_students = Stream(students).filter(lambda x: x['school'] == '武汉大学').to_list()
    pprint(whu_students)


def chain_using_map_and_filter():
    # 筛选出武汉大学的学生，并将年龄大于21的学生的姓名映射为大写
    whu_students_names = (
        Stream(students)
        .filter(lambda x: x['school'] == '武汉大学')
        .filter(lambda x: x['age'] > 21)
        .map(lambda x: "三国：" + x['name'])
        .to_list()
    )

    pprint(whu_students_names)


if __name__ == '__main__':
    # filter_by_school()
    chain_using_map_and_filter()
