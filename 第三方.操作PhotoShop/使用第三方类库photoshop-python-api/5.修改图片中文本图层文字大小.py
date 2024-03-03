"""
 * @file   : 5.修改图片中文本图层文字大小.py
 * @time   : 9:18
 * @date   : 2024/1/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.biz.adobe.photoShopHelper import PhotoShopHelper
from BasicLibrary.io.fileShadowUsing import FileShadowUsing
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper
from photoshop import Session

if __name__ == '__main__':
    project_root = ProjectHelper.get_root_physical_path()
    local_path = r"操作PhotoShop/使用第三方类库photoshop-python-api/_res/"
    psd_file_full_name = PathHelper.combine(project_root, local_path, "textUsing.psd")

    with FileShadowUsing(psd_file_full_name) as shadow_file_full_name:
        with Session(shadow_file_full_name, action="open") as ps:
            app = ps.app
            doc = ps.app.activeDocument

            my_layer = PhotoShopHelper.find_layer(doc, "TextDemo")
            my_layer.textItem.size = 30
        pass

    pass
