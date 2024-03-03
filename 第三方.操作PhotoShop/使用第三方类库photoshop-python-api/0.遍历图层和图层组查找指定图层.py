"""
 * @file   : 遍历图层和图层组查找指定图层.py
 * @time   : 18:12
 * @date   : 2023/11/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import photoshop.api as ps
from BasicLibrary.projectHelper import ProjectHelper
from BasicLibrary.biz.adobe.photoShopHelper import PhotoShopHelper


if __name__ == '__main__':
    # 打开PhotoShop应用程序
    app = ps.Application()

    # 打开指定的图片文件
    root_path = ProjectHelper.get_root_physical_path()
    file_path = f'{root_path}\\操作PhotoShop\\使用第三方类库photoshop-python-api\\_res\\multi-layer.psd'
    doc = app.open(file_path)

    _layers = doc.layers
    # 1. 按照图层索引查找指定的图层
    _layer_code = 0
    _found_layer = PhotoShopHelper.find_layer(doc, _layer_code)

    if _found_layer:
        print(f"找到指定图层: {_found_layer.name}")
    else:
        print(f"未找到指定图层: {_layer_code}")
    pass

    # 2. 按照给定的图层名称查找指定的图层（系统会自动遍历各个图层组，查找到第一个符合条件名称的图层）
    _layer_code = '图层 6'  # 替换为你要查找的图层名称
    _found_layer = PhotoShopHelper.find_layer(doc, _layer_code)

    if _found_layer:
        print(f"找到指定图层: {_found_layer.name}")
    else:
        print(f"未找到指定图层: {_layer_code}")
    pass

    # 3. 按照给定的图层名称路径查找指定的图层
    _layer_code = 'MyGroup1//图层 5'
    _found_layer = PhotoShopHelper.find_layer(doc, _layer_code)

    if _found_layer:
        print(f"找到指定图层: {_found_layer.name}")
    else:
        print(f"未找到指定图层: {_layer_code}")
    pass

    # 关闭图片文件
    doc.close()
