import re
from builtins import *


# ————————————————
# 版权声明：本文为CSDN博主「艾莉宝贝」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_42793426/article/details/88545939
def compile_with_match(content, pattern):
    regex = re.compile(pattern)
    result = regex.match(content)

    display_result(result)


def compile_with_search(content, pattern):
    regex = re.compile(pattern)
    result = regex.search(content)

    display_result(result)


def compile_with_findall(content, pattern):
    regex = re.compile(pattern)
    result = regex.findall(content)

    display_result(result)


def only_match(content, pattern):
    result = re.match(pattern, content)
    display_result(result)


def only_search(content, pattern):
    result = re.search(pattern, content)
    display_result(result)


def only_findall(content, pattern):
    result = re.findall(pattern, content)
    display_result(result)


def display_result(calculated_result):
    print(calculated_result)
    print(type(calculated_result))

    if calculated_result:
        if type(calculated_result) is list:
            print(f'结果是一个字符数组，内容为{calculated_result}')
        else:
            print(calculated_result.group())
            print(calculated_result.span())
    else:
        print('NNN没有匹配成功')

    print("─────────────────────────────────────")


if __name__ == '__main__':
    _pattern = r'\w*a\w*'
    _content = 'Hello, I am Jack, from Chongqing, a mountain city, nice to meet you……'

    print('以下是调用compile和match配合的结果')
    compile_with_match(_content, _pattern)

    print('以下是单独调用match的结果')
    only_match(_content, _pattern)

    print('以下是调用compile和search配合的结果')
    compile_with_search(_content, _pattern)

    print('以下是单独调用search的结果')
    only_search(_content, _pattern)

    print('以下是调用compile和findall配合的结果')
    compile_with_findall(_content, _pattern)

    print('以下是单独调用findall的结果')
    only_findall(_content, _pattern)

    _pattern = r'\w*o\w*'
    print('以下是单独调用match的结果')
    only_match(_content, _pattern)
