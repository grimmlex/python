# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)


def get_three_bubbles(start_point, radius=50, step=0):
    for _ in range(3):
        sd.circle(start_point, radius + step)
        radius += step


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def get_bubble(start_point, count=1, radius=50, step=0):
    for _ in range(count):
        sd.circle(start_point, radius + step)
        radius += step


# Нарисовать 10 пузырьков в ряд

def get_ten_bubbles():
    x1 = 150
    for _ in range(10):
        start_point = sd.get_point(x1, 200)
        sd.circle(start_point)
        x1 += 100


# get_ten_bubbles()
# Нарисовать три ряда по 10 пузырьков
def get_thirty_bubbles():
    x = 150
    y = 200
    for _ in range(3):
        for _ in range(10):
            start_point = sd.get_point(x, y)
            sd.circle(start_point)
            x += 100
        x = 150
        y += 100


# get_thirty_bubbles()
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

def get_hundred_bubbles():
    for _ in range(100):
        sd.circle(sd.random_point(), color=sd.random_color())
        x = random


get_hundred_bubbles()
sd.pause()
