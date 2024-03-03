"""
 * @file   : _util.py
 * @time   : 16:24
 * @date   : 2023/12/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 1. 本代码是Photoshop脚本开发的基础代码，可以用于快速开发Photoshop脚本
# 2. 代码中包含了一些常用的函数和类，可以用于处理Photoshop脚本开发中的常见问题
# 3. 本文件中经过验证的功能，要迁移至`BasicLibrary.PY`中，为其他项目共用
# +--------------------------------------------------------------------------

class PsUtil(object):

    @classmethod
    def display_layer_property(cls, layer):
        if layer:
            print('layer.name:', layer.name)
            print('layer.visible:', layer.visible)
            print('layer.isBackgroundLayer:', layer.isBackgroundLayer)
            print('layer.positionLocked:', layer.positionLocked)
            print('layer.pixelsLocked:', layer.pixelsLocked)
            print('layer.transparentPixelsLocked:', layer.transparentPixelsLocked)
            print('layer.allLocked:', layer.allLocked)
        else:
            print('layer is None')

    pass


pass
