import pyautogui
import time


'''while True:  #option to do like Hotkey/shortcut but takes to much energy.
    if keyboard.is_pressed('d') and keyboard.is_pressed('u') and keyboard.is_pressed('b') and keyboard.is_pressed('a') and keyboard.is_pressed('i') and keyboard.is_pressed('1'):'''

pyautogui.press('win')
time.sleep(0.5)
pyautogui.click(x=747, y=164, duration=0.1)
pyautogui.typewrite('microsoft edge')
time.sleep(0.5)
pyautogui.click(x=1063, y=581, duration=0.1)
time.sleep(0.7)
pyautogui.hotkey('win', 'right')
pyautogui.click(x=1850, y=10, duration=0.1)
pyautogui.typewrite('https://www.youtube.com/watch?v=ahy5o5nT4oI')
pyautogui.press('enter')
pyautogui.click(x=370, y=17, duration=0.1)
pyautogui.typewrite('https://www.youtube.com/watch?v=eQo_tJdZMkI')
pyautogui.press('enter')
pyautogui.click(x=200, y=17, duration=0.1)
time.sleep(2)
'pyautogui.click(x=238, y=875, duration=0.2)' #to mute
pyautogui.press('space')
time.sleep(1)
pyautogui.press('f')
'''pyautogui.click(x=1723, y=1041, duration=1.5)        #quali auf 1440 p aber geht nicht immer
pyautogui.click(x=1714, y=947, duration=0.1)
pyautogui.click(x=1693, y=510, duration=0.1)'''
