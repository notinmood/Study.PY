"""
 * @file   : index.py
 * @time   : 10:52
 * @date   : 2024/3/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

import tomlkit
from BasicLibrary.data.tomlMate import TomlMate
from tomlkit import TOMLDocument

# from 各种格式文件的读写操作.TOML操作.tomlMate import TomlMate


if __name__ == '__main__':
    here = os.path.abspath(os.path.dirname(__file__))
    toml_file_full_name = os.path.join(here, "_res", "my.toml")

    with open(toml_file_full_name, 'r', encoding="utf-8") as file:
        toml_doc: TOMLDocument = tomlkit.load(file)
        print(type(toml_doc))
        print(toml_doc)

        version = toml_doc["tool"]["poetry"]["version"]
        print(version)

        print(toml_doc.get("tool/poetry"))

        print("──分割线───────────────────────────────────")
        tool = toml_doc.get("tool")
        print(tool)
        poetry = tool.get("poetry")
        print(poetry)

        dependencies = poetry.get("dependencies")
        print(dependencies)

        version = poetry.get("version")
        print(version)
        print("──分割线───────────────────────────────────")

        mate = TomlMate(toml_file_full_name)
        value = mate.get("tool/poetry/version")
        print(value)

        value = mate.get("tool/poetry/version2")
        print(value)

        value = mate.get("tool/poetry2/version")
        print(value)

        # toml_doc["myproject"]["version"] = "0.2.2"
        print("──分割线───────────────────────────────────")
        toml_doc["tool"]["poetry"]["version"] = "0.2.1"

        node_path = "tool/poetry/version"
        print(mate.get(node_path))

        with open(toml_file_full_name, "w", encoding="utf-8") as f:
            f.write(toml_doc.as_string())
        pass

        mate.set(node_path, "0.2.3")
    pass
