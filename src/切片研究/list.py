"""
 * @file   : list.py
 * @time   : 15:57
 * @date   : 2021/12/4
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.environment.consoleHelper import ConsoleHelper

if __name__ == '__main__':
    list_data = [1, 3, 5, 7, 9]
    print(list_data[:-1])
    ConsoleHelper.echo(list_data[1:])
