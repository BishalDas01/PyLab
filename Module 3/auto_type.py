import pyautogui
from time import sleep
sleep(5)

for i in range(0,100):
    pyautogui.write('bal', interval=0)
    pyautogui.press('enter')

