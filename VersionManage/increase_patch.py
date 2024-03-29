"""
 * @file   : increase_patch.py
 * @time   : 17:53
 * @date   : 2024/3/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from BasicLibrary.data.tomlMate import TomlMate
from BasicLibrary.projectHelper import ProjectHelper

from VersionManage.versionHelper import VersionHelper


def execute():
    root_path = ProjectHelper.get_root_physical_path()
    toml_file_full_name = os.path.join(root_path, "pyproject.toml")

    mate = TomlMate(toml_file_full_name)

    node_path = "tool/poetry/version"
    old_version = mate.get(node_path)
    print(old_version)

    new_version = VersionHelper.increase_patch(old_version)
    mate.set(node_path, new_version)
    print(new_version)


pass

if __name__ == '__main__':
    execute()
