# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1000, 700)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smile():
    for _ in range(10):
        point1 = sd.random_number(55, 900)
        point2 = sd.random_number(55, 650)
        center = sd.get_point(point1, point2)
        sd.circle(center, 55)
        center = sd.get_point(point1 - 20, point2 + 20)
        sd.circle(center, 10)
        center = sd.get_point(point1 + 20, point2 + 20)
        sd.circle(center, 10)
        center = sd.get_point(point1 - 20, point2 - 20)
        center1 = sd.get_point(point1 + 20, point2 - 20)
        point_list = [center, center1]
        sd.lines(point_list)


draw_smile()

sd.pause()
