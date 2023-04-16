# -*- coding: utf-8 -*-

from colorama import init
from random import randint
from termcolor import cprint

init(autoreset=True)


class House:
    count = 0
    all_food = 0
    num_coat = 0

    def __init__(self):
        self.money = 100
        self.food = 100
        self.cat_food = 30
        self.dirt = 0
        self.all_money = self.money


    def __str__(self):
        self.dirt += 5
        self.count += 1
        if self.count == 365:
            print(f'{self.all_money} - денег заработано, {self.all_food} - еды съедено, {self.num_coat} - шуб куплено')

        return f"В доме: денег - {self.money}, еды в холодильнике - {self.food}, грязи - {self.dirt}, " \
               f"еды для кота - {self.cat_food}"


class Human:
    def __init__(self):
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.name = None
        self.total_food = 0
        self.death = False

    # def __str__(self):
    #     return f'Я {self.name} - моя сытость {self.fullness}, моё счастье {self.happiness}'

    def eat(self):
        if self.total_food > self.house.food:
            self.total_food = self.house.food
            self.fullness += self.total_food
            self.house.food -= self.total_food
        else:
            self.fullness += self.total_food
            self.house.food -= self.total_food
        self.house.all_food += self.total_food
        # print(f'{self.name} поел(а), {self.total_food} единиц')

    def pet_cat(self):
        self.happiness += 5

    def act(self):
        if self.fullness <= 0:
            self.death = True
            return False
        if self.happiness < 10:
            self.death = True
            return False
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 15:
            self.eat()
            return False
        return True


class Husband(Human):
    def __init__(self, name, house, salary):
        super().__init__()
        self.name = name
        self.house = house
        self.salary = salary

    # def __str__(self):
    #     return super().__str__()

    def eat(self):
        self.total_food = randint(1, 30)
        super().eat()

    def work(self):
        self.fullness -= 10
        self.house.money += self.salary
        self.house.all_money += self.salary

        # print(f'{self.name} пошёл на работу')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        # print(f'{self.name} играет')

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
                # return print(f'{self.name} смотрел телевизор с женой целый день')
        elif self.happiness < 10:
            return print(f'{self.name} умер от депрессии')
        elif self.fullness <= 0:
            return print(f'{self.name} умер от голода')


class Wife(Human):

    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house

    # def __str__(self):
    #     return super().__str__()

    def eat(self):
        self.total_food = randint(1, 30)
        super().eat()

    def shopping(self):
        if self.house.money < 50:
            return print(f'Деньги кончились')
        self.fullness -= 10
        self.house.food += 50
        self.house.money -= 50
        if self.house.cat_food < 100:
            if self.house.money < 100:
                return print(f'Деньги кончились')
            self.house.cat_food += 100
            self.house.money -= 100
            # return print(f'{self.name} пошла за покупками и купила еды коту')
        # print(f'{self.name} пошла за покупками')

    def buy_fur_coat(self):
        if self.house.money > 350:
            self.fullness -= 10
            self.house.money -= 350
            self.house.num_coat += 1
            self.happiness += 60
            # print(f'{self.name} решила купить себе пальто.)')
        else:
            self.happiness -= 10
            # print(f'{self.name} хотела купить себе пальто. Но денег нет)')

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt > 150:
            self.house.dirt -= 100
        else:
            self.house.dirt -= self.house.dirt
        # print(f'{self.name} убралась в доме')

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
                # return print(f'{self.name} смотрела телевизор с мужем целый день')
        elif self.happiness < 10:
            return print(f'{self.name} умер от депрессии')
        elif self.fullness <= 0:
            return print(f'{self.name} умер от голода')


class Cat:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 10
        self.house = house
        self.death = False

    # def __str__(self):
    #     return f'Я {self.name} - моя сытость {self.fullness}'

    def act(self):
        if self.fullness < 0:
            self.death = True
            return print(f'{self.name} умер от голода')
        if self.fullness < 10:
            return self.eat()
        dice = randint(1, 3)
        if dice == 1:
            return self.soil()
        else:
            return self.sleep()

    def eat(self):
        if self.happiness == 0:
            self.death = True
            return print(f'{self.name} Умер')
        if self.house.cat_food > 0:
            total_food = randint(1, 10)
            if self.house.cat_food > total_food:
                self.fullness += total_food * 2
                self.house.cat_food -= total_food
            else:
                total_food = self.house.cat_food
                self.house.cat_food -= total_food
            # print(f'{self.name} поел.')
        else:
            self.happiness -= 10
            self.death = True
            return print(f'{self.name} Умер')

    def sleep(self):
        self.fullness -= 10
        # print(f'{self.name} спит.')

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        # print(f'{self.name} нашкодил.')


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
        # print(f'{self.name} поспал(а)')


# home = House()
#
# humans = [
#     Husband(name='Сережа', house=home),
#     Wife(name='Маша', house=home),
# ]
#
# cats = []
#
# for i in range(1, 5):
#     cats.append(Cat(name=f"Кот #{i}", house=home))
#
# kids = [
#     Kid(name='Борис', house=home)
# ]
#
# for day in range(365):
#     cprint(f'================== День {day + 1} ==================', color='red')
#     for human in humans:
#         human.act()
#     for cat in cats:
#         cat.act()
#     for kid in kids:
#         kid.act()
#     for human in humans:
#         cprint(human, color='cyan')
#     for cat in cats:
#         cprint(cat, color='cyan')
#     for kid in kids:
#         cprint(kid, color='cyan')
#
#     print(home)

class Simulation():

    def __init__(self, money_incidents, food_incidents):
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents

    def experiment(self, salary):
        num_cat = 1
        max_cat = 0
        sucsess = True
        money_incidents_count = 0
        food_incidents_count = 0

        while sucsess:
            home = House()

            humans = [
                Husband(name='Сережа', house=home, salary=salary),
                Wife(name='Маша', house=home),
            ]

            cats = []

            for i in range(num_cat):
                cats.append(Cat(name=f"Кот #{i + 1}", house=home))

            kids = [
                Kid(name='Борис', house=home)
            ]
            count = 0
            money_random_days = []
            for i in range(money_incidents_count):
                money_random_days.append(randint(1, 365))
            food_random_days = []
            for i in range(food_incidents_count):
                food_random_days.append(randint(1, 365))
            for day in range(365):
                for i in money_random_days:
                    if i == day:
                        home.money = home.money/2
                for i in food_random_days:
                    if i == day:
                        home.food = home.food / 2
                for human in humans:
                    human.act()
                if human.death:
                    sucsess = False
                    break
                for cat in cats:
                    cat.act()
                if cat.death:
                    sucsess = False
                    break
                for kid in kids:
                    kid.act()
                count += 1
            if count == 365:
                max_cat = num_cat
                num_cat += 1
            else:
                sucsess = False

        return max_cat
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов

for food_incidents in range(6):
  for money_incidents in range(6):
      life = Simulation(money_incidents, food_incidents)
      for salary in range(50, 401, 50):
          max_cats = life.experiment(salary)
          cprint(f'При зарплате {salary} максимально можно прокормить {max_cats} котов', color= "red")