import pyautogui

import time

pyautogui.PAUSE = 0.8

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")


link = "https://www.youtube.com/watch?v=BxKahT39AGA"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)
