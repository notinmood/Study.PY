"""
 * @file   : 3.更换图片功能.py
 * @time   : 15:40
 * @date   : 2024/1/2
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
    psd_file_full_name = PathHelper.combine(project_root, local_path, "replace_images.psd")
    new_pic_full_name = PathHelper.combine(project_root, local_path, "red_100x200.png")

    with FileShadowUsing(psd_file_full_name) as _res:
        with Session(_res, action="open") as ps:
            # 查找并设置活动图层
            target_layer = PhotoShopHelper.find_layer(ps.active_document, "green_130x260")
            ps.active_document.activeLayer = target_layer

            active_layer = ps.active_document.activeLayer
            original_bounds = active_layer.bounds
            print(f"current layer {active_layer.name}: {original_bounds}")

            replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
            id_null = ps.app.charIDToTypeID("null")
            action_descriptor = ps.ActionDescriptor
            action_descriptor.putPath(id_null, new_pic_full_name)
            ps.app.executeAction(replace_contents, action_descriptor)

            # replaced image.
            active_layer = ps.active_document.activeLayer
            current_bounds = active_layer.bounds
            original_width = original_bounds[2] - original_bounds[0]
            original_height = original_bounds[3] - original_bounds[1]

            current_width = current_bounds[2] - current_bounds[0]
            current_height = current_bounds[3] - current_bounds[1]
            size_rate = original_width / current_width * 100
            active_layer.resize(size_rate, size_rate, ps.AnchorPosition.MiddleCenter)
            print(f"current layer {active_layer.name}: {current_bounds}")

            ps.active_document.save()
            # # 暂时不关闭，开发人员可以直接查看是否复制图层成功
            # ps.active_document.close()
        pass
    pass
