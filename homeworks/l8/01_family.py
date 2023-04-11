# -*- coding: utf-8 -*-

from colorama import init
from random import randint
from termcolor import cprint

init(autoreset=True)


class House:

    def __init__(self):
        self.money = 100
        self.food = 100
        self.cat_food = 30
        self.dirt = 0
        self.all_money = self.money
        self.all_food = 0
        self.num_coat = 0

    def __str__(self):
        self.dirt += 5
        return f'В доме: денег - {self.money}, еды в холодильнике - {self.food}, грязи - {self.dirt}, еды для кота - ' \
               f'{self.cat_food}'


class Human:
    def __init__(self):
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.name = None
        self.total_food = 0

    def __str__(self):
        return f'Я {self.name} - моя сытость {self.fullness}, моё счастье {self.happiness}'

    def eat(self):

        if self.total_food > self.house.food:
            self.total_food = self.house.food
            self.fullness += self.total_food
            self.house.food -= self.total_food
        else:
            self.fullness += self.total_food
            self.house.food -= self.total_food
        self.house.all_food += self.total_food
        print(f'{self.name} поел(а), {self.total_food} единиц')

    def pet_cat(self):
        self.happiness += 5

    def act(self):
        if self.fullness <= 0:
            return False
        if self.happiness < 10:
            return False
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 15:
            self.eat()
            return False
        return True


class Husband(Human):
    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house

    def __str__(self):
        return super().__str__()

    def eat(self):
        self.total_food = randint(1, 30)
        super().eat()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        self.house.all_money += 150

        print(f'{self.name} пошёл на работу')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        print(f'{self.name} играет')

    def act(self):
        result = super().act()
        if result:
            if self.house.money <= 100:
                return self.work()
            if self.happiness < 20:
                return self.gaming()
            dice = randint(1, 3)
            if dice == 1:
                self.work()
            elif dice == 2:
                self.gaming()
            else:
                self.fullness -= 10
                return print(f'{self.name} смотрел телевизор с женой целый день')
        elif self.happiness < 10:
            return print(f'{self.name} умер от депрессии')
        elif self.fullness < 10:
            return print(f'{self.name} умер от голода')


class Wife(Human):

    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house

    def __str__(self):
        return super().__str__()

    def eat(self):
        self.total_food = randint(1, 30)
        super().eat()

    def shopping(self):
        self.fullness -= 10
        self.house.food += 50
        self.house.money -= 50
        if self.house.cat_food < 10:
            self.house.cat_food += 20
            self.house.money -= 20
            return print(f'{self.name} пошла за покупками и купила еды коту')
        print(f'{self.name} пошла за покупками')

    def buy_fur_coat(self):
        if self.house.money > 350:
            self.fullness -= 10
            self.house.money -= 350
            self.house.num_coat += 1
            self.happiness += 60
            print(f'{self.name} решила купить себе пальто.)')
        else:
            print(f'{self.name} хотела купить себе пальто. Но денег нет)')

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt > 150:
            self.house.dirt -= 100
        else:
            self.house.dirt -= self.house.dirt
        print(f'{self.name} убралась в доме')

    def act(self):
        result = super().act()
        if result:
            dice = randint(1, 4)
            # if self.house.money > 350
            if self.house.food < 50:
                return self.shopping()
            if self.happiness < 20:
                return self.buy_fur_coat()
            if self.house.dirt > 100:
                return self.clean_house()
            if dice == 1:
                return self.clean_house()
            elif dice == 2:
                return self.shopping()
            elif dice == 3:
                return self.buy_fur_coat()
            else:
                self.fullness -= 10
                return print(f'{self.name} смотрела телевизор с мужем целый день')
        elif self.happiness < 10:
            return print(f'{self.name} умер от депрессии')
        elif self.fullness < 10:
            return print(f'{self.name} умер от голода')


class Cat:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return f'Я {self.name} - моя сытость {self.fullness}'

    def act(self):
        if self.fullness < 0:
            return print(f'{self.name} умер от голода')
        if self.fullness < 10:
            return self.eat()
        dice = randint(1, 3)
        if dice == 1:
            return self.soil()
        else:
            return self.sleep()

    def eat(self):
        total_food = randint(1, 10)
        if self.house.cat_food > total_food:
            self.fullness += total_food * 2
            self.house.cat_food -= total_food
        else:
            total_food = self.house.cat_food
            self.house.cat_food -= total_food
        print(f'{self.name} поел.')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} спит.')

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        print(f'{self.name} нашкодил.')


class Kid(Human):

    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house
        self.total_food = randint(1, 10)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 10:
            return self.eat()
        else:
            return self.sleep()

    def eat(self):
        self.total_food = randint(1, 10)
        super().eat()

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} поспал(а)')


home = House()

humans = [
    Husband(name='Сережа', house=home),
    Wife(name='Маша', house=home),
]

cats = [
    Cat(name='Барсик', house=home),
]
kids = [
    Kid(name='Борис', house=home)
]
for day in range(365):
    cprint(f'================== День {day + 1} ==================', color='red')
    for human in humans:
        human.act()
    for cat in cats:
        cat.act()
    for kid in kids:
        kid.act()
    for human in humans:
        cprint(human, color='cyan')
    for cat in cats:
        cprint(cat, color='cyan')
    for kid in kids:
        cprint(kid, color='cyan')

    cprint(home, color='cyan')

print(f'{home.all_money} - денег заработано, {home.all_food} - еды съедено, {home.num_coat} - шуб куплено')

# Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)
#
# class Child:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass

# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(3):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')