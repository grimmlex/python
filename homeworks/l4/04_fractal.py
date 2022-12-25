# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

start_point = sd.get_point(200, 10)
start_angle = 90
length = 150


def draw_branches(point, angle, length):
    while length < 10:
        return
    branch = sd.get_vector(start_point = point, angle = angle, length = length)
    branch.draw()
    next_point = branch.end_point
    next_angle = angle - sd.random_number(-60, 60)
    next_length = length * (sd.random_number(60, 75)/100)
    draw_branches(next_point, next_angle, next_length)
    draw_branches(next_point, next_angle, next_length)

for delta in range(0, 70, 5):
    draw_branches(start_point, start_angle, 150)

# draw_branches(start_point, start_angle, 100,)
# draw_branches(start_point, start_angle, 200)
# draw_branches(start_point, start_angle, 120)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


