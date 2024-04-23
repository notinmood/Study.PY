"""
 * @file   : 01.入门.py
 * @time   : 上午6:55
 * @date   : 2024/4/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import pyautogui

if __name__ == '__main__':
    # 禁止PyAutoGUI的失败安全机制
    pyautogui.FAILSAFE = False

    # 显示鼠标位置
    print(pyautogui.position())

    # 显示屏幕尺寸
    print(pyautogui.size())

    # 移动鼠标到屏幕左上角
    pyautogui.moveTo(0, 0)

    # 点击鼠标左键
    pyautogui.click()

    # 移动鼠标到屏幕右下角
    pyautogui.moveTo(1366, 768)

    # 点击鼠标右键
    pyautogui.click(button='right')
pass
