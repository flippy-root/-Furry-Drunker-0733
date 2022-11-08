from tkinter import *
from tkinter.messagebox import *

# класс Paint
class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        # Параметры кисти по умолчанию
        self.brush_size = 10
        self.brush_color = "red"
        self.color = "red"
        # Устанавливаем компоненты UI
        self.setUI()

        # Метод рисования на холсте

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

        # Изменение цвета кисти

    def set_color(self, new_color):
        self.color = new_color

        # Изменение размера кисти

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def setUI(self):
        # Устанавливаем название окна
        self.parent.title("Demo Paint")
        # Размещаем активные элементы на родительском окне
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        # Создаем холст с белым фоном
        self.canv = Canvas(self, bg="white")

        # Приклепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке,
        # и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и
        # заставляем растягиваться при растягивании всего окна

        self.canv.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)

        # задаем реакцию холста на нажатие левой кнопки мыши
        self.canv.bind("<B1-Motion>", self.draw)

        # создаем метку для кнопок изменения цвета кисти
        color_lab = Label(self, text="Цвет: ")

        # Устанавливаем созданную метку в первый ряд и первую колонку,
        # задаем горизонтальный отступ в 6 пикселей
        color_lab.grid(row=0, column=0, padx=6)

        # создание кнопки: установка текста кнопки, задание ширины кнопки (10 символов)
        red_btn = Button(self, text="Красный", width=10, command=lambda: self.set_color("red"))

        # устанавливаем кнопку в первый ряд, вторая колонка
        red_btn.grid(row=0, column=1)

        # по аналогии создаем остальные кнопки
        green_btn = Button(self, text="Зеленый", width=10, command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Синий", width=10, command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="черный", width=10, command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="Белый", width=10, command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        # Создаем метку для кнопок изменения размера кисти
        size_lab = Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2x", width=10, command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="5x", width=10, command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="7x", width=10, command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="10x", width=10, command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="20x", width=10, command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="50x", width=10, command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)

        clear_btn = Button(self, text="Очистить", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

# выход из программы  
def close_win():
  if askyesno("Выход", "Вы уверены?"):
    root.destroy()

# вывод справки    
def about():
  showinfo("Demo Paint", "Paint.exe")
  
# функция для создания главного окна
def main():
    global root
    root = Tk()
    root.geometry("800x600+300+300")
    app = Paint(root)
    m = Menu(root)
    root.config(menu=m)

    fm = Menu(m)
    m.add_cascade(label="Файл", menu=fm)
    fm.add_command(label="Выход", command=close_win)

    hm = Menu(m)
    m.add_cascade(label="Справка", menu=hm)
    hm.add_command(label="О программе", command=about)
    root.mainloop()

if __name__ == "__main__":
    main()
