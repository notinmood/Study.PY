"""
 * @file   : 2.复制图层功能.py
 * @time   : 8:12
 * @date   : 2024/1/1
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.io.fileShadowUsing import FileShadowUsing
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper
from BasicLibrary.biz.adobe.photoShopHelper import PhotoShopHelper

import photoshop.api as psapi

if __name__ == '__main__':
    project_root = ProjectHelper.get_root_physical_path()
    local_path = r"操作PhotoShop/使用第三方类库photoshop-python-api/_res/layerPropertyStudy.psd"
    file_full_name = PathHelper.combine(project_root, local_path)

    with FileShadowUsing(file_full_name) as res_full_name:
        app = psapi.Application()

        # 打开指定的图片文件
        doc = app.open(res_full_name)

        my_layer = PhotoShopHelper.find_layer(doc, "签名1")

        if my_layer:
            my_layer.visible = False

            new_layer = my_layer.duplicate()
            new_layer.visible = True
            new_layer.name = "落款-百度"

            wechat_layer = PhotoShopHelper.find_layer(doc, "公众号：文句之美 拷贝")
            if wechat_layer:
                wechat_layer.visible = True

                # 同时设置图层的name和textItem.contents可以使二者分别展示不同信息
                wechat_layer.name = ">公众号：文句之美"
                wechat_layer.textItem.contents = ">>百家号：故事里的人生智慧"
            pass
        pass

        # # 暂时不关闭，开发人员可以直接查看是否复制图层成功
        # doc.close()
    pass
