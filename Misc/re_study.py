import re
from builtins import *

from hiland.data import StringHelper as rgh
from hiland.io import IOHelper as ioh


def get_file_names():
    target_dir = "C:\\bb\\cc"
    result = ioh.get_files(target_dir, False)

    return result


def remove_html_tag(original_html):
    patten = rgh.patten_html_tag()
    data = re.sub(patten, "", original_html)
    return data


def format_content(original_content):
    patten = r'(\d+[\.|,|、])'
    data = rgh.add_padding(original_content, patten, "\r\n")
    return data


def regex_demo():
    original = "6. 佛说：苦海无涯，回头是岸。放下屠刀，立地成佛。7. 你不要一直不满人家，要一直检讨自己才对。不满人家是苦了你自己。"
    patten = r'\d+[\.|,|、]'
    result = rgh.add_padding(original, patten, "*=*", False)
    print(result)


def store_demo():
    content = "Hello,Mr. Shu!"
    file_name = "C:\\bb\\cbc\\1.txt"
    ioh.store_file(file_name, content, False)


def add_newline():
    content = ioh.load_file("C:\\bb\\fo.txt")
    patten = r'(佛说)'
    data = rgh.add_padding(content, patten, "\r\n")
    print(data)


def read_file_with_lines():
    content = ioh.load_file_with_lines("C:\\bb\\fo.txt")
    print(content)


def __line_callback(line):
    print(line)
    print('-=' * 10)


def read_file_with_line():
    ioh.load_file_with_line("C:\\bb\\fo.txt", __line_callback)


# def match_start_digit(original):
#     my_pattern = r'^\d+\.'
#     groups = re.match(my_pattern, original)
#     result = groups.group(0)
#     my_number = StringHelper.get_before_content(result, ".")
#     my_info = StringHelper.get_after_content(original, result)
#     my_info = StringHelper.remove_head(my_info)
#     print(f"{my_number}===={my_info}")
#     # print(ObjectHelper.get_type(mm))
#     # print(mm)
#     return my_number, my_info


if __name__ == '__main__':
    help(re.compile)
# _original = '59. If necessary, I am willing to manipulate people to get what I want. '
# aa = match_start_digit(_original)
# print(aa[0])
# read_file_with_line()
# read_file_with_lines()
# add_newline()
# store_demo()

# file_name = "C:\\bb\\cc\\1.txt"
# print(os.path.splitext(file_name))
# print(os.path.split(file_name))
# print("555555555555555555")
#
# ext_name = ioh.get_file_ext_name(file_name)
# print(ext_name)
#
# short_name = ioh.get_file_short_name(file_name)
# print(short_name)
#
# path_name = ioh.get_file_path_name(file_name)
# print(path_name)
# f_name = os.path.join(path_name, short_name)
# print(f_name)

# path_name = "C:\\bb\\bbb\\"
# ioh.ensure_path(path_name)

# regex_demo()

# files = get_file_names()
# for file in files:
#     _original_content = ioh.load_file(file)
#     _result = remove_html_tag(_original_content)
#     _result = format_content(_result)
#     path_name = "C:\\bb\\ccd"
#     ioh.ensure_path(path_name)
#     new_file_name = os.path.join(path_name, ioh.get_file_short_name(file))
#     ioh.store_file(new_file_name, _result)
