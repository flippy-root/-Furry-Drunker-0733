while True:
    # Using Keyboard module in Python
    import keyboard
    from colorama import init, Fore, Back, Style
    import os
    import time
    import tkinter
    from tkinter.constants import *
    import re
    from tkinter import *
    import mouse
    # It writes the content to output
    # получим объект файла
    file1 = open("exemple.txt", "+a")
    file1 = open("exemple.txt", "r")
    print(Style.BRIGHT + Fore.BLUE + "CHEESE:")
    def upi2():
        while True:
            line = file1.readline()
            print("MODE: click")
            print(" key: ")
            print(Style.BRIGHT + Fore.GREEN + line.strip())
            print("press 'alt' ")
            keyboard.wait('alt')
            # считываем строку
            # прерываем цикл, если строка пустая
            if not line:
                break
            # выводим строку
            print(Style.BRIGHT + Fore.RED + " LOST FILE: ")
            print(line.strip())
            print(Style.BRIGHT + Fore.BLACK + " return: ")
            keyboard.write(line.strip())
            time.sleep(1)
            keyboard.press('space')
            time.sleep(2)
            keyboard.press('enter')
        file1.close
    def upi():
        print("MODE: avto")
        print(Style.BRIGHT + Fore.RED + "INPUT NUMBER:")
        x = int(input())
        print("press 'alt' ")
        keyboard.wait('alt')
        while True:
            # считываем строку
            mouse.click('left')
            time.sleep(x)
            for i in range(100):
                keyboard.press('Backspace')
            time.sleep(x)
            line = file1.readline()
            print(Style.BRIGHT + Fore.GREEN + " key: ")
            print(line.strip())
            time.sleep(x)
            # прерываем цикл, если строка пустая
            if not line:
                break
            # выводим строку
            print(Style.BRIGHT + Fore.RED + " LOST FILE: ")
            print(line.strip())
            print(Style.BRIGHT + Fore.BLACK + " return: ")
            keyboard.write(line.strip())
            time.sleep(x)
            mouse.click('left')
            time.sleep(x)
            keyboard.press('space')
            time.sleep(2)
            keyboard.press('enter')
            time.sleep(2)
        file1.close
    def upi3():
        file1.close
        time.sleep(10)
        file1 = open("exemple.txt", "+a")
        file1 = open("exemple.txt", "r")
        print(Style.BRIGHT + Fore.BLUE + "RETURN:")
    window = Tk()  
    window.title("keyboard")  
    btn = Button(window, text="avto", command=upi)  
    btn.grid(column=1, row=0)
    btn = Button(window, text="click", command=upi2)  
    btn.grid(column=1, row=1)
    btn = Button(window, text="return", command=upi3)  
    btn.grid(column=1, row=2)
    window.mainloop()


