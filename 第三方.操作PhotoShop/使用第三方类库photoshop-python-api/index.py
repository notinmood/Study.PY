import os

import photoshop.api as psapi
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.io.fileHelper import FileHelper
from photoshop.api import ExportOptionsSaveForWeb, ExportType


def deal_detail_file(full_path_file_name, new_date_4_layer):
    # 指定要查找的layer名字
    layer_name = '@20230816'

    #  获取文件full_path_file_name的扩展名
    ext_name = FileHelper.get_extension_name(full_path_file_name)
    # 如果扩展名ext_name 不是".psd"，那么就跳出
    if ext_name != ".psd":
        return
    pass

    # 打开指定的图片文件
    doc = app.open(full_path_file_name)
    # 获取所有图层
    layers = doc.layers
    # 遍历图层列表，找到需要操作的图层
    for layer in layers:
        if layer.name == layer_name:  # 替换为你想要操作的图层名称
            layer.visible = True

            # 更改图层内容
            layer.textItem.contents = new_date_4_layer  # "@20231206"
        pass
    pass

    # 保存修改后的图片
    doc.save()
    opts = ExportOptionsSaveForWeb()
    file_name_4_export = StringHelper.replace(full_path_file_name, ".psd", ".png")
    doc.exportDocument(file_name_4_export, ExportType.SaveForWeb, opts)
    # 关闭图片文件
    doc.close()


pass

if __name__ == '__main__':
    # 打开PhotoShop应用程序
    app = psapi.Application()

    file = r'E:\cc\13.psd'
    deal_detail_file(file, "@20231206")
