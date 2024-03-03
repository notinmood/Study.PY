"""
 * @file   : base64模块内的方法1.encode和decode.py
 * @time   : 11:09
 * @date   : 2024/1/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import base64
import os

from BasicLibrary.data.base64Helper import Base64Helper

# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# base64.encode/decode是对文件的编码解码操作
# +--------------------------------------------------------------------------

if __name__ == '__main__':
    here = os.path.abspath(os.path.dirname(__file__))

    # 1. 编码
    txt_original_file_path = os.path.join(here, "_res/test_txt_original.txt")
    image_original_file_path = os.path.join(here, "_res/test_image_original.png")

    txt_encoded_file_path = os.path.join(here, "_res/test_txt_encoded.byte")
    image_encoded_file_path = os.path.join(here, "_res/test_image_encoded.byte")

    # inputRead = open(txt_original_file_path, 'rb')
    # outputWrit = open(txt_encoded_file_path, 'wb')
    # base64.encode(inputRead, outputWrit)
    #
    # inputRead = open(image_original_file_path, 'rb')
    # outputWrit = open(image_encoded_file_path, 'wb')
    # base64.encode(inputRead, outputWrit)

    Base64Helper.encode_file(txt_original_file_path, txt_encoded_file_path)
    Base64Helper.encode_file(image_original_file_path, image_encoded_file_path)

    # 2. 解码
    txt_encoded_file_path = os.path.join(here, "_res/test_txt_encoded.byte")
    txt_decoded_file_path = os.path.join(here, "_res/test_txt_decoded.txt")

    image_encoded_file_path = os.path.join(here, "_res/test_image_encoded.byte")
    image_decoded_file_path = os.path.join(here, "_res/test_image_decoded.png")

    # inputRead = open(txt_encoded_file_path, 'rb')
    # outputWrit = open(txt_decoded_file_path, 'wb')
    # base64.decode(inputRead, outputWrit)
    #
    # inputRead = open(image_encoded_file_path, 'rb')
    # outputWrit = open(image_decoded_file_path, 'wb')
    # base64.decode(inputRead, outputWrit)

    Base64Helper.decode_file(txt_encoded_file_path, txt_decoded_file_path)
    Base64Helper.decode_file(image_encoded_file_path, image_decoded_file_path)
pass
