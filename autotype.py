import pyautogui
import time
time.sleep(10)
for i in range(200):
    pyautogui.typewrite("India ktna runs bnayega ? "+str(i+150)+" runs?")
    pyautogui.press("enter")
