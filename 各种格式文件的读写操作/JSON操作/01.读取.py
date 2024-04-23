"""
 * @file   : 01.读取.py
 * @time   : 上午10:00
 * @date   : 2024/4/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import json
from pathlib import Path

if __name__ == '__main__':

    here = Path(__file__).resolve().parent
    json_file = here / '_res' / 'jianying_draft_content.json'

    # 读取json文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    pass

    # 访问materials下的transitions数组
    transitions = data['materials']['transitions']

    # 遍历transitions数组，打印每个元素的name和resource_id
    for transition in transitions:
        print(f"Name: {transition['name']}, Resource ID: {transition['resource_id']}")
        # print(f"\"{transition['name']}\": \"{transition['resource_id']}\",")
    pass
