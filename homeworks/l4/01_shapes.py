# -*- coding: utf-8 -*-

import simple_draw as sd

lenght = 300


def draw_shapes(x, y, z):
    start_point = sd.get_point(x, y)
    angle = 0
    if z == 4:
        v1 = sd.get_vector(start_point, angle)
        v1.draw()
        end = v1.end_point
        for num in range(z - 1):
            angle += 90
            v = sd.get_vector(end, angle)
            v.draw()
            end = v.end_point
    if z == 3:
        v1 = sd.get_vector(start_point, angle)
        v1.draw()
        end = v1.end_point
        for num in range(z - 1):
            angle += 120
            v = sd.get_vector(end, angle)
            v.draw()
            end = v.end_point


draw_shapes(100, 10, 5)
draw_shapes(400, 10, 3)

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


sd.pause()
