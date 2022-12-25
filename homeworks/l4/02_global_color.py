# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом


colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
colors_name = ["Красный - 1", "Оранжевый - 2", "Жёлтый - 3", "Зелёный - 4", "Сине-зелёный -5", "Голубой - 6",
               "Розовый - 7"]


def get_color():
    print(colors_name)
    color = int(input("Введите номер цвета"))
    return colors[color - 1]

def draw_shapes(x, y, z, color, width):
    start_point = sd.get_point(x, y)
    angle = 0
    if z == 4:
        v1 = sd.get_vector(start_point, angle, width = width)
        v1.draw(color)
        end = v1.end_point
        for num in range(z - 1):
            angle += 90
            v = sd.get_vector(end, angle, width = width)
            v.draw(color)
            end = v.end_point
    if z == 3:
        v1 = sd.get_vector(start_point, angle, width = width)
        v1.draw()
        end = v1.end_point
        for num in range(z - 1):
            angle += 120
            v = sd.get_vector(end, angle, width = width)
            v.draw()
            end = v.end_point

c = get_color()

draw_shapes(100, 100, 4, c, 3)
sd.pause()
