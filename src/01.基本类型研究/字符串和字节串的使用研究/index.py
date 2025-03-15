"""
 * @file   : index.py
 * @time   : 16:17
 * @date   : 2024/1/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import base64

from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper

if __name__ == '__main__':
    print(base64.b64encode(b'binary\x00string'))
    # 以下是为了消除ide的警告而做的cheating
    # noinspection all
    print(base64.b64decode(b'YmluZ3M='))
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xac\x42\xd5\x02\xb1\x80\x09'))
    print(base64.urlsafe_b64decode('abcd--__'))
    # 以下是为了消除ide的警告而做的cheating
    # noinspection all
    # base64.b64encode(b'binary\x00string')

    print("──分割线───────────────────────────────────")
    response = b'<h1>Hello World!</h1>'
    print(response)
    print(response.decode())
    print(base64.b64encode(response))

    print("──分割线───────────────────────────────────")

    root_path = ProjectHelper.get_root_physical_path()
    image_full_name = PathHelper.combine(root_path, "_res", "00.人民日报.Cover.jpg")
    print(f"图片文件{image_full_name}的base64编码： ")
    with open(image_full_name, "rb") as f:
        print(base64.b64encode(f.read()).decode())
    pass
