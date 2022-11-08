import os
import time
print("second (Move)")
x = int(input()) 
while True:   
    file1 = open("listAnm.txt", "a+")
    file1 = open("listAnm.txt", "r")
    # считываем все строки
    lines = file1.readlines()
    # итерация по строкам
    print("start list...")
    print("start system...")
    for line in lines:
        print("cod:")
        print(line.strip())  
        os.system('title ' + line.strip())
        time.sleep(x)
# закрываем файл
    os.system('cls')
    file1.close()
