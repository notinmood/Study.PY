"""
 * @file   : index.py
 * @time   : 17:02
 * @date   : 2024/1/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import base64
import requests
import json

from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper

from UmiOCR使用.returnResult import ReturnResult


def ocr_image(image_file_full_name: str) -> str:
    """
    调用本地Umi-ORC软件的API接口
    :param image_file_full_name:
    :return:
    """
    with open(image_file_full_name, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    pass

    headers = {'Content-Type': 'application/json'}
    data = {
        "base64": image_data
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    rr = ReturnResult(status=True, message="ok", data=None)

    if response.status_code == 200:
        res_dict = json.loads(response.text)

        code = res_dict["code"]
        if code == 101:
            rr.data = ""
            return rr
        pass

        if code == 100:
            data_list = res_dict["data"]
            if not data_list:
                rr.data = ""
            else:
                rr.data = ""
                for _item in data_list:
                    rr.data += _item["text"]
                pass
            pass

            return rr
        pass

        rr.status = False
        rr.message = "OCR识别错误"
        rr.data = None
        return rr
    pass

    rr.status = False
    rr.message = "网络访问错误"
    rr.data = None
    return rr


if __name__ == '__main__':
    print("以下是调用本地Umi-ORC软件的API接口的示例：")

    url = "http://127.0.0.1:1224/api/ocr"
    root_path = ProjectHelper.get_root_physical_path()
    image_full_name = PathHelper.combine(root_path, "_res", "00.人民日报.Cover.jpg")
    result: ReturnResult = ocr_image(image_full_name)
    if result.status:
        print(result.data)
    else:
        print(result.message)
    pass
