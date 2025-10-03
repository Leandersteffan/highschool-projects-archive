import datetime
import time
import pyautogui
from tkinter import *


class ImOff:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('ImOff Kalender')
        self.main_window.geometry('300x90')
        self.main_window.configure(background='gray')
        'Label'
        self.description_La = Label(text='Willst du den ImOff Kalender vervollständigen lassen')
        self.description_La.place(x='10', y='5')
        'Button'
        self.yes_Bu = Button(text='Ja', background='green', command=self.yes)
        self.yes_Bu.place(x='10', y='50')
        self.no_Bu = Button(text='Nein', background='red', command=self.no)
        self.no_Bu.place(x='250', y='50')

        self.main_window.mainloop()

    def yes(self):
        global target_year, target_month, target_day
        self.kalender_aktualisieren()
        a = datetime.date(target_year, target_month, target_day)
        while True:
            a += datetime.timedelta(days=1)
            if a.weekday() == 0:
                break
        target_year = a.year
        target_month = a.month
        target_day = a.day
        with open('C:\A\Programmieren\Eigene Projekte\ImOff_Aktualisierung_Zwischenspeicher\clipboard.txt', 'r+') as f:
            f.write(f'{target_year}\n')
            f.write(f'{target_month}\n')
            f.write(f'{target_day}\n')
        self.main_window.destroy()

    def no(self):
        self.main_window.destroy()

    def kalender_aktualisieren(self):
        pyautogui.press('win')
        time.sleep(0.5)
        pyautogui.click(x=747, y=164, duration=0.1)
        pyautogui.typewrite('microsoft edge')
        time.sleep(1)
        pyautogui.click(x=1063, y=581, duration=0.1)
        time.sleep(1.5)
        pyautogui.hotkey('win', 'right')
        pyautogui.click(x=1850, y=10, duration=1)
        pyautogui.typewrite('https://app.im-off.de/external/extras/calendar')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=71, y=748, duration=0.1)
        pyautogui.click(x=218, y=758, duration=0.1)
        pyautogui.click(x=343, y=752, duration=0.1)
        pyautogui.click(x=476, y=749, duration=0.1)
        pyautogui.click(x=608, y=758, duration=0.1)
        pyautogui.click(x=717, y=753, duration=0.1)
        pyautogui.click(x=851, y=761, duration=0.1)
        pyautogui.click(x=900, y=786, duration=0.1)
        pyautogui.click(x=905, y=874, duration=0.1)
        pyautogui.click(x=338, y=22, duration=1)

with open('C:\A\Programmieren\Eigene Projekte\ImOff_Aktualisierung_Zwischenspeicher\clipboard.txt', 'r') as f:
    target_year = f.readline()
    target_year = int(target_year)
    target_month = f.readline()
    target_month = int(target_month)
    target_day = f.readline()
    target_day = int(target_day)

while True:
    now = datetime.datetime.today()
    target = datetime.datetime(target_year, target_month, target_day, 0, 0, 0)
    if target <= now:
        a = ImOff()







    time.sleep(10)
