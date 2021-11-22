import config as cfg

import pyautogui


def delete_bg(dtime=0.5):
    # type(dtime) >> float
    position = cfg.positions["Buttons"]["Copy"]

    pyautogui.moveTo(position, duration=dtime)
    pyautogui.click()
