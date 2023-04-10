# -*- coding: utf-8 -*-

import simple_draw as sd

width = 1200
height = 800
sd.resolution = (width, height)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self, length, num):
        self.length = length
        self.snowflakes = []
        self.i = 0
        self.num = num

    # def gen_snowflake(self):
    #     for _ in range(self.num):
    #         self.snowflakes.append({'length': self.length, 'x': sd.randint(10, width - 10),
    #                                 'y': height + sd.randint(100, 150)})
    #     return self.snowflakes

    def gen_snowflakes(self):
        return {'length': self.length, 'x': sd.randint(10, width - 10), 'y': height + sd.randint(100, 150)}
    def run_snowfall(self):
        for _ in range(self.num):
            self.snowflakes.append(self.gen_snowflakes())
        # sd.draw_background()
        while True:
            # sd.clear_screen()
            for snowflake in self.snowflakes:
                point = sd.get_point(snowflake['x'], snowflake['y'])
                sd.snowflake(point, snowflake['length'], sd.background_color)

                snowflake['x'] -= sd.randint(-10, 10)
                snowflake['y'] -= sd.randint(10, 25)

                point = sd.get_point(snowflake['x'], snowflake['y'])
                sd.snowflake(point, snowflake['length'], sd.COLOR_WHITE)

                if snowflake['y'] < sd.randint(0, 40):
                    self.snowflakes.remove(snowflake)

            self.i += 1
            if self.i % 2 == 0:
                self.snowflakes.append(self.gen_snowflakes())

            sd.sleep(0.1)
            if sd.user_want_exit():
                break


snow = Snowflake(55, 5)
snow.run_snowfall()



# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
