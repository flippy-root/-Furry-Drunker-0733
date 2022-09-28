from PIL import Image, ImageColor
from PIL import ImageDraw
import os
i = 0
while True:
    os.system('cls')
    print("width")
    width = int(input())
    print("height")
    height = int(input())

    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

# Заполним все изображение белым цветом
    draw.rectangle((0, 0, width-1, height-1), fill=ImageColor.getrgb("white"), outline=ImageColor.getrgb("black"))


    def function1(x):
        return 5 * (x ** 2) + x ** 3 - x ** 4


    class Point:  # создал класс для удобства
        def __init__(self, x, y):
            self.x = x
            self.y = y


# задаем область значений функции
    print("start_x")
    start_x = int(input())
    print("end_x")
    end_x = int(input())
    print("start_y")
    start_y = int(input())
    print("end_y")
    end_y = int(input())

    points = []

    x = start_x
    step_x = 0.1

    while x <= end_x:  # проходим по всей ширине
        y = function1(x)  # вычисляем значение функции для текущего значения x
        points.append(Point(x, y))  # добавляем эту точки в список точек
        x += step_x


# И так у нас есть список точек функции в заданном регионе. Как таблица значений функции в школе.
# Все точки в системе координат функции.

    def convert(point):
    # Напишем функцию которая будет конвертировать точку в системе координат функции, в нашу систему координат
    # У нас вся ширина 400, а графика функции в нашей области от -4 до 4 - 8 единиц
    # Поэтому вычислим масштаб по x и по y: т.е. во сколько раз ширина изображения больше ширины графика

        scale_x = width / (end_x - start_x)
        scale_y = height / (end_y - start_y)

    # Зная мастшаб, мы вычисляем координаты в нашей системе координат для текущей точки
        local_x = point.x * scale_x
        local_y = point.y * scale_y

    # Помните что, у нас центры разные? Перемещаем центр точек Так как начало графика по x -4, мы должны
    # умножить -4 на машстаб и сдвинуть точки на 4 значения правее (поэтому с минусом).
    # и точно также сдвигаем по y
        local_x = (-start_x * scale_x) + local_x
        local_y = (-start_y * scale_y) + local_y

    # Создаем новую точку в нашей системе координат. И переворичваем Y. Сами догадайтесь почему.
        return Point(local_x, height - local_y)

# рисуем оси координат
    start_hor = convert(Point(start_x, 0))
    end_hor = convert(Point(end_x, 0))
    draw.line((start_hor.x, start_hor.y, end_hor.x, end_hor.y), fill=ImageColor.getrgb("green"))

    start_ver = convert(Point(0, start_y))
    end_ver = convert(Point(0, end_y))
    draw.line((start_ver.x, start_ver.y, end_ver.x, end_ver.y), fill=ImageColor.getrgb("red"))

# рисуем на экране все точки.
    print("Start point")
    for point in points:
        i = i + 1
        current_point = convert(point)
        draw.line((last_point.x, last_point.y, current_point.x, current_point.y), fill=ImageColor.getrgb("blue"))
        last_point = current_point
        print("Loud_point:",i)
    print("export")
    image.save("graphic.png", "PNG")
    print("New point: graphic.png!")
