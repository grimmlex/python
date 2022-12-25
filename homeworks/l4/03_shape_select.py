# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код

colors = {
    1: (sd.COLOR_RED, 'red'),
    2: (sd.COLOR_ORANGE, 'orange'),
    3: (sd.COLOR_YELLOW, 'yellow'),
    4: (sd.COLOR_GREEN, 'green'),
    5: (sd.COLOR_CYAN, 'cyan'),
    6: (sd.COLOR_BLUE, 'blue'),
    7: (sd.COLOR_PURPLE, 'purple'),
}

shapes = {
    1: (3, "triangle"),
    2: (4, "square"),
    3: (5, "pentagon"),
    4: (6, "hexagon"),
}


def get_color():
    for key in colors.keys():
        print(key, ":", colors[key][1])
    color = int(input("Введите номер цвета: "))
    return colors[color][0]

def get_shapes():
    for key in shapes.keys():
        print(key, ":", shapes[key][1])
    shape = int(input("Выбирите фигуру: "))
    return shapes[shape][0]


def draw_shapes(x, y, z, color, width):
    start_point = sd.get_point(x, y)
    angle = 0
    if z == 3:
        v1 = sd.get_vector(start_point, angle, width = width)
        v1.draw(color)
        end = v1.end_point
        for num in range(z-1):
            angle += 120
            v = sd.get_vector(end, angle, width = width)
            v.draw(color)
            end = v.end_point
    if z == 4:
        v1 = sd.get_vector(start_point, angle, width = width)
        v1.draw(color)
        end = v1.end_point
        for num in range(z - 1):
            angle += 90
            v = sd.get_vector(end, angle, width = width)
            v.draw(color)
            end = v.end_point
    if z == 5:
        v1 = sd.get_vector(start_point, angle, width = width)
        v1.draw(color)
        end = v1.end_point
        for num in range(z - 1):
            angle += 72
            v = sd.get_vector(end, angle, width = width)
            v.draw(color)
            end = v.end_point
    if z == 6:
        v1 = sd.get_vector(start_point, angle, width = width)
        v1.draw(color)
        end = v1.end_point
        for num in range(z - 1):
            angle += 60
            v = sd.get_vector(end, angle, width = width)
            v.draw(color)
            end = v.end_point


draw_shapes(200, 200, get_shapes(), get_color(), 3)

sd.pause()
