# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (700, 500)


# sd.rectangle(left_bottom, right_top, color= sd.COLOR_DARK_ORANGE, width=3)

y1 = 0
y2 = 50
i = 0

for _ in range(10):
    i += 1
    color = sd.COLOR_ORANGE
    x1 = 0
    x2 = 100
    if i % 2 == 0:
        x1 = -50
        x2 = 50
    for _ in range(7):
        left_bottom = sd.get_point(x1, y1)
        right_top = sd.get_point(x2, y2)
        sd.rectangle(left_bottom, right_top, color, width=1)
        x1 += 100
        x2 += 100

    y1 += 50
    y2 += 50

sd.pause()