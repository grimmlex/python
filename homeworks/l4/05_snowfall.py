# -*- coding: utf-8 -*-
# import pygame
import simple_draw as sd
from random import random, randint

width = 1200
height = 800
sd.resolution = (width, height)

# Можно задать фоновое изображение. Нужно подключить библиотеку pygame и
# придется при каждой (или через двет-три) итерации  while перерисовывать фон
# раскомментировать строки 2, 13 и 56

# sd._background_image = pygame.image.load('001.jpg')

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# N = 5

N = 5


def gen_snowflake():
    return { 'length': sd.random_number(10,100),
             'x': sd.randint(10, width - 10),
             'y': height + sd.randint(100, 150)
            }


snowflakes = []

for _ in range(N):
    snowflakes.append(gen_snowflake())

i = 0

while True:
    # sd.clear_screen()
    # sd.draw_background()

    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(
            point, snowflake['length'],
            sd.background_color)

        snowflake['x'] -= sd.randint(-10, 10)
        snowflake['y'] -= sd.randint(10, 25)

        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(
            point, snowflake['length'],
            sd.COLOR_WHITE)
        if snowflake['y'] < sd.randint(0, 40):
            snowflakes.remove(snowflake)
    i += 1
    if i % 2 == 0:
        snowflakes.append(gen_snowflake())



    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

sd.pause()
