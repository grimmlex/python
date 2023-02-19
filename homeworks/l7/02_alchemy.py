# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    count = 0

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Lava):
            return Stone()

    def __str__(self):
        return "Water"


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()

    def __str__(self):
        return "Air"


class Fire:
    def __str__(self):
        return "Fire"

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()


class Earth:
    def __str__(self):
        return "Earth"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()


class Storm:
    def __str__(self):
        return "Storm"


class Vapor:
    def __str__(self):
        return "Vapor"


class Dirt:
    def __str__(self):
        return "Dirt"


class Lightning:
    def __str__(self):
        return "Lightning"


class Dust:
    def __str__(self):
        return "Dust"


class Lava:
    def __str__(self):
        return "Lava"

    def __add__(self, other):
        if isinstance(other, Water):
            return Stone()


class Stone:
    def __str__(self):
        return "Stone"


water = Water()
lava = Lava()

# print(Fire(), '+', Air(), '=', Fire() + Air())
# print(Fire(), '+', Air(), '=', Fire() + Air())
# print(Water(), '+', Earth(), '=', Water() + Earth())
# print(Water, '+', Lava, '=', Water + Lava)
print(water + lava)
# print(Water(), '+', Dust(), '=', Water() + Dust())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
