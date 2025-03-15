"""
 * @file   : 2.给图层解锁的实践.py
 * @time   : 16:08
 * @date   : 2024/1/4
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.biz.adobe.photoShopHelper import PhotoShopHelper
from BasicLibrary.io.fileShadowUsing import FileShadowUsing
from BasicLibrary.io.pathHelper import PathHelper
from photoshop import Session
from _utils.psUtil import PsUtil

if __name__ == '__main__':
    file_base_name_no_extension = 'layerPropertyStudy'
    file_extension_name = '.psd'
    file_base_name = file_base_name_no_extension + file_extension_name
    current_path = PathHelper.get_dir_name(__file__, 1)
    res_path = PathHelper.combine(current_path, "_res")
    file_full_name = PathHelper.combine(res_path, file_base_name)

    with FileShadowUsing(file_full_name) as shadow_file_full_name:
        with Session(shadow_file_full_name, action="open") as ps:
            app = ps.app
            doc = ps.app.activeDocument
            layers = doc.layers

            print("1. 给普通图层锁定位置")
            my_layer = PhotoShopHelper.find_layer(doc, 0)
            PsUtil.display_layer_property(my_layer)
            my_layer.positionLocked = True
            PsUtil.display_layer_property(my_layer)

            print("──分割线───────────────────────────────────")

            print("2. 展示给锁定位置的图层解锁")
            my_layer = PhotoShopHelper.find_layer(doc, "签名1//公众号：文句之美")
            PsUtil.display_layer_property(my_layer)
            my_layer.positionLocked = False
            PsUtil.display_layer_property(my_layer)

            print("──分割线───────────────────────────────────")

            print("3. 展示给锁定像素的图层解锁")
            my_layer = PhotoShopHelper.find_layer(doc, "签名1//getqrcode-文句之美-灰色")
            PsUtil.display_layer_property(my_layer)
            my_layer.pixelsLocked = False
            PsUtil.display_layer_property(my_layer)

            print("──分割线───────────────────────────────────")

            print("4. 展示被父图层锁定的子图层的解锁")
            # +--------------------------------------------------------------------------
            # |::::TIPS::::| 本代码的使用说明
            # ---------------------------------------------------------------------------
            # 可以发现，通过父图层锁定子图层后，仅仅在子图层上执行解锁操作是无效的。
            # +--------------------------------------------------------------------------
            my_layer = PhotoShopHelper.find_layer(doc, "签名2//公众号：文句之美")
            PsUtil.display_layer_property(my_layer)
            my_layer.positionLocked = False
            PsUtil.display_layer_property(my_layer)

            print("──分割线───────────────────────────────────")

            print("5. 展示展示被父图层锁定的子图层的循环解锁")
            my_layer = PhotoShopHelper.find_layer(doc, "签名2//公众号：文句之美")
            PsUtil.display_layer_property(my_layer)
            PhotoShopHelper.unlock(doc, "签名2//公众号：文句之美")
            PsUtil.display_layer_property(my_layer)

        pass
    pass
