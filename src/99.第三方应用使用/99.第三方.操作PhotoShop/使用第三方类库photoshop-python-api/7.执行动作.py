"""
 * @file   : 7.执行动作.py
 * @time   : 17:33
 * @date   : 2024/1/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from photoshop import Session

if __name__ == '__main__':
    with Session() as api:
        api.app.doAction(action="Action1", action_from="My")
    pass
pass
