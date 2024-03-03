"""
 * @file   : 1.py
 * @time   : 17:12
 * @date   : 2024/3/2
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

import ffmpeg
from BasicLibrary.projectHelper import ProjectHelper

if __name__ == '__main__':
    root_path = ProjectHelper.get_root_physical_path()
    middle_path = r"操作FFMPEG\_res"

    input_file = os.path.join(root_path, middle_path, 'input.mp4')
    output_file = os.path.join(root_path, middle_path, 'output.mp4')

    # 裁剪前十秒
    (ffmpeg
     .input(input_file)
     .trim(start=0, duration=10)
     .output(output_file)
     .run())
