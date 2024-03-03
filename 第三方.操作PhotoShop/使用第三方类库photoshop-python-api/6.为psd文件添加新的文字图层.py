# TODO:xiedali@2024/01/17 暂时无法实现，目前通过调用 ps动作的方式曲线实现（即现在ps的动作内建立文字图层，然后再通过Python调用这个动作执行）

# """
#  * @file   : 6.为psd文件添加新的文字图层.py
#  * @time   : 16:25
#  * @date   : 2024/1/17
#  * @mail   : 9727005@qq.com
#  * @creator: ShanDong Xiedali
#  * @company: HiLand & RainyTop
# """
# from BasicLibrary.biz.adobe.photoShopHelper import PhotoShopHelper
# from BasicLibrary.io.fileShadowUsing import FileShadowUsing
# from BasicLibrary.io.pathHelper import PathHelper
# from BasicLibrary.projectHelper import ProjectHelper
# from photoshop import Session
# from photoshop.api import RGBColor
# from photoshop.api._artlayer import ArtLayer
#
# if __name__ == '__main__':
#     project_root = ProjectHelper.get_root_physical_path()
#     local_path = r"操作PhotoShop/使用第三方类库photoshop-python-api/_res/"
#     psd_file_full_name = PathHelper.combine(project_root, local_path, "addTextLayer.psd")
#
#     with FileShadowUsing(psd_file_full_name) as shadow_file_full_name:
#         with Session(shadow_file_full_name, action="open") as ps:
#             app = ps.app
#             doc = ps.app.activeDocument
#
#             # document = ps.active_document
#             # # Create color object of color red.
#             # fillColor = ps.SolidColor()
#             # fillColor.rgb.red = 222
#             # fillColor.rgb.green = 0
#             # fillColor.rgb.blue = 0
#             # # Add a new layer called Background.
#             # layer = document.artLayers.add()
#             # layer.name = "Background"
#             # # Select the entire layer.
#             # document.selection.selectAll()
#             # # Fill the selection with color.
#             # document.selection.fill(fillColor)
#             # # Deselect.
#             # document.selection.deselect()
#
#             my_layer = doc.artLayers.add()
#             my_layer.name = "TitleSignature"
#
#             my_layer = PhotoShopHelper.find_layer(doc, "TitleSignature")
#
#             # my_layer.kind = "Text"
#             my_layer.textItem.contents = "你好，中国"
#             # my_layer.textItem.contents = "你好，中国"
#             # my_layer.textItem.font = "仿宋"
#             # my_layer.textItem.size = 35
#             # my_layer.textItem.color = RGBColor(0, 0, 0)
#             # my_layer.textItem.position = (100, 100)
#             # my_layer.textItem.alignment = "Center"
#             # my_layer.textItem.lineHeight = 1.2
#             # my_layer.textItem.paragraphSpacing = 0
#             # my_layer.textItem.paragraphIndent = 0
#             # my_layer.textItem.characterSpacing = 0
#             # my_layer.textItem.textDecoration = "None"
#             # my_layer.textItem.textCase = "None"
#             # my_layer.textItem.textKerning = "Default"
#             # my_layer.textItem.textLeading = "Default"
#             # my_layer.textItem.textRendering = "Always Anti-Alias"
#             # my_layer.textItem.textStroke = "None"
#
#             # ps.active_document.artLayers.add(my_layer)
#
#             # doc.save()
#         pass
#     pass
#
# pass
