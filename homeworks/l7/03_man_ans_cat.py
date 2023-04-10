# -*- coding: utf-8 -*-
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py
# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
from colorama import init, Fore, Back, Style
from termcolor import cprint, colored
from random import randint
init(autoreset=True)


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print(colored('{} поел'.format(self.name), color='yellow'))
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        print(Fore.MAGENTA + '{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def get_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_bowl += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        if self.fullness > 20:
            print(f'{self.name} Убрал за {self.house.cat}')
            self.house.cat_dirt -= 100
            self.fullness -= 20
        else:
            cprint('{} Устал!'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 100:
            self.work()
        elif self.house.cat_bowl < 50:
            self.get_cat_food()
        elif self.house.cat_dirt > 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def get_cat(self):
        for cat in cats:
            if cat.name == self.house.cat:
                return

            self.house.cat = cat.name
            cat.house = self.house
            print(f"{self.name} завёл кота {self.house.cat}")


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat = 0
        self.cat_bowl = 0
        self.cat_dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, грязно {}, в кошачьей миске осталось {}'.format(
            self.food, self.money, self.cat_dirt, self.cat_bowl)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.house = None

    def __str__(self):
        return 'Я - кот {}, сытость {}'.format(
            self.name, self.fullness)

    def sleep(self):
        print(f"{self.name} поспал!")
        self.fullness -= 10

    def eat(self):
        print(f"{self.name} поел!")
        self.fullness += 20
        self.house.cat_bowl -= 10

    def scratches_wallpaper(self):
        print(f"{self.name} нашкодил!")
        self.fullness -= 10
        self.house.cat_dirt += 10

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 2 or dice == 1:
            self.scratches_wallpaper()
        else:
            self.sleep()

citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

cats = [
    Cat(name="Мурзик"),
    Cat(name="Барсик"),
]

my_sweet_home = House()

for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)

citizens[randint(0, len(citizens)) - 1].get_cat()

for day in range(1, 366):
    cprint('================ день {} =================='.format(day), color= "green")
    for citizen in citizens:
        citizen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)
