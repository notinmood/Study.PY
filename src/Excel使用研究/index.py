"""
 * @file   : index.py
 * @time   : 15:25
 * @date   : 2022/3/14
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import datetime

import xlwings
from BasicLibrary import ObjectHelper
from BasicLibrary.io.pathHelper import PathHelper
from xlwings import Sheet

from _projectHelper import ProjectHelper


def operate_excel():
    root = ProjectHelper.get_root_physical_path()
    file_name = r"Excel使用研究\_res\myExcel.xlsx"
    # file_full_name = r"E:\myworkspace\MyStudy\Python\Excel使用研究\_res\myExcel.xlsx"
    file_full_name = PathHelper.combine(root, file_name)
    """
    两种打开 Excel 文件的方式，推荐使用第一种。因为第二种容易出现 文件正被占用无法使用的问题。
    """

    # 打开 Excel 的 工作簿 Book 的方式 1
    app = xlwings.App(False)
    my_book = app.books.open(file_full_name)

    # # 打开 Excel 的 工作簿 Book 的方式 2
    # my_book = xlwings.Book(file_full_name)

    print("────以下显示book的信息─────────────────────────────────")
    print(ObjectHelper.get_type(my_book))
    print(my_book)
    if isinstance(my_book, xlwings.Book):
        # print("YY")
        print("────以下显示各个sheet信息─────────────────────────────────")
        for key in my_book.sheets:
            print(key)

        print("────以下显示第一个sheet信息─────────────────────────────────")
        my_sheet = my_book.sheets[0]
        print(my_sheet)

        print("────以下显示各个sheet信息─────────────────────────────────")
        if isinstance(my_sheet, Sheet):
            print(my_sheet.cells)

            '''
            一. 读取
            '''
            '''
            每次可以读一个区域：参数一个或两个：
                如果一个参数的时候就仅仅访问一个单元格的range，这个参数就是这个单元格的坐标
                如果两个参数的时候分别为一个区域的左上角和右下角的单元格坐标
            '''
            print(my_sheet.range("A1").value)  # 单个值信息 '姓名'
            print(my_sheet.range("A1", "A2").value)  # 一维数组 ['姓名', '张三']
            print(my_sheet.range("A1", "B1").value)  # 一维数组 ['姓名', '年龄']

            print(my_sheet.range("A1", "B2").value)  # 二维数组 [['姓名', '年龄'], ['张三', 20.0]]
            print(my_sheet.range("A1:B2").value)  # 二维数组 [['姓名', '年龄'], ['张三', 20.0]]

            """
            每次仅能访问一个格子：
                两个参数为：行名称和列名称（注意行名称前面，列名称后面）
            """
            print(my_sheet.cells(1, 'A').value)  # 单个值信息 '姓名'
            print(my_sheet.cells('1', 'A').value)  # 单个值信息 '姓名'

            """
            二. 写入
            """
            """
            2.1 按照 range 写入
            """

            """
            2.1.1 当个数值的写入
            """
            my_data = datetime.datetime.now()
            my_sheet.range("G5").value = my_data
            print(my_data)
            print(my_sheet.range("G5").value)

            """
            2.1.2 同一行内写入和读取 都是一维数组            
            """
            my_sheet.range("G8:H8").value = ["g8", "h8"]
            print(my_sheet.range("G8:H8").value)  # ['g8', 'h8']

            """
            2.1.3 跨行内写入的是二维数值；读取的是一维数组。（请特别注意）         
            """
            my_sheet.range("G6:G7").value = [["G6"], ["G7"]]
            print(my_sheet.range("G6:G7").value)  # ['G6', 'G7']

            """
            2.1.4 多行多列的读写
            """
            my_sheet.range("G9:H10").value = [['g9', 'h9'], ['g10', 'h10']]
            print(my_sheet.range("G9:H10").value)  # [['g9', 'h9'], ['g10', 'h10']]

            """
            2.1.00 仅仅指定开始位置，xlwings 自动推断出一个范围进行写入
            """
            my_sheet.range("G13").value = [['g13', 'h13'], ['g14', 'h14']]
            print(my_sheet.range("G13:H14").value)

            """
            2.2 按照 cell 写入
            """
            my_sheet.cells("5", "H").value = my_data
            print(my_sheet.cells("5", "H").value)
    else:
        print("NN")

    my_book.save()
    my_book.close()


if __name__ == '__main__':
    operate_excel()
