# -*- coding: utf-8 -*-
from pprint import pprint

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pyparsing import *


class Parser:

    def __init__(self, name):
        self.file_name = name
        self.dict = {}

    def openfile(self, out_file_name=None):
        if out_file_name is not None:
            out_file = open(out_file_name, 'w')
        else:
            out_file = None

        with open(self.file_name, 'r', encoding='cp1251') as file:
            if out_file:
                date = Word(nums + "- :")
                self_time = Word('.' + nums)
                word = Word('NOK')
                parse_module = (Suppress('[') + date + Suppress(self_time) + Suppress(']') + Suppress(word))('event_time')
                result = OneOrMore(Group(parse_module))
                datafile = result.parseString(file.read()).asList()
                for item in datafile:
                    if item[0][:-3] in self.dict:
                        self.dict[item[0][:-3]] += 1
                    else:
                        self.dict[item[0][:-3]] = 1
                for key, value in self.dict.items():
                    out_file.write(str(f'{key} {value}\n'))
        if out_file:
            out_file.close()


p1 = Parser('events.txt')
p1.openfile(out_file_name='out.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
