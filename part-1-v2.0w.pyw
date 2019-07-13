from threading import Thread
from tkinter import *  
from tkinter.ttk import Radiobutton  
import time
from time import strftime, localtime, sleep #Для (Time)
import struct, ctypes #Для (def Wallpaper)
import os #Для (SCRIPT_DIRECTORY)

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))#Путь- (part-1)

#print(SCRIPT_DIRECTORY)

Cycle01 = 0

#/////////////////////////////////////////////////////////////////////




def functt(haha):
    e = 0
    e2 = 0
    e3 = 0
    e4 = 0
    def Wallpaper():
        SPI_SETDESKWALLPAPER = 20
        if r == (1):
            WALLPAPER_PATH = SCRIPT_DIRECTORY + '\\Время\\Morning.png'

        if r == (2):
            WALLPAPER_PATH = SCRIPT_DIRECTORY + '\\Время\\Day.jpg'

        if r == (3):
            WALLPAPER_PATH = SCRIPT_DIRECTORY + '\\Время\\Evening.png'

        if r == (4):
            WALLPAPER_PATH = SCRIPT_DIRECTORY + '\\Время\\Night.png'


        def is_64_windows():
            """Find out how many bits is OS. """
            return struct.calcsize('P') * 8 == 64


        def get_sys_parameters_info():
            """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
            return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
                else ctypes.windll.user32.SystemParametersInfoA


        def change_wallpaper():
            sys_parameters_info = get_sys_parameters_info()
            r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

            # When the SPI_SETDESKWALLPAPER flag is used,
            # SystemParametersInfo returns TRUE
            # unless there is an error (like when the specified file doesn't exist).
            if not r:
                print(ctypes.WinError())


        change_wallpaper()

    #//////////////////////////////////////////////////////////////////////////////



    while Cycle01 != 1:
        Time = (strftime("%H", localtime()))#Сколько часов ?
        #print(Time)
        Time_int = int(Time)
        #print(a1)
        if Time_int >= 6:    #Утро 6-12
            if Time_int <= 12:
                if e == 0:
                    r = 1
                    e = 1
                    e2 = 0
                    e3 = 0
                    e4 = 0
                    Wallpaper()

        if Time_int >= 13:   #День 13-17
            if Time_int <= 17:
                if e2 == 0:
                    r = 2
                    e = 0
                    e2 = 1
                    e3 = 0
                    e4 = 0
                    Wallpaper()

        if Time_int >= 18:   #Вечер 18-20
            if Time_int <= 20:
                if e3 == 0:
                    r = 3
                    e = 0
                    e2 = 0
                    e3 = 1
                    e4 = 0
                    Wallpaper()

        if Time_int >= 21:#Ночь 21-5
            if e4 == 0:
                r = 4
                e = 0
                e2 = 0
                e3 = 0
                e4 = 1
                Wallpaper()
        if Time_int <= 5:#Ночь 21-5(2)
            if e4 == 0:
                r = 4
                e = 0
                e2 = 0
                e3 = 0
                e4 = 1
                Wallpaper()
        
        sleep(60)#Остановка на 60 сек.

def b():
    global Cycle01
    Cycle01 = 1


def a():
    global Cycle01
    Cycle01 = 0
    variable = Thread(target=functt, args=('ahhah',))
    variable.start()



window = Tk()  
window.title("part-1w.pyw")  
window.geometry('400x250')  
rad1 = Radiobutton(window, text='Вкл', value=1, command=a)  
rad2 = Radiobutton(window, text='Выкл', value=2, command=b)  
rad1.grid(column=0, row=0)  
rad2.grid(column=1, row=0)  
window.mainloop()