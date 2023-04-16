# -*- coding: utf-8 -*-
from pprint import pprint
from tabulate import tabulate
# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Charstats:
    char_stats = {}

    def __init__(self):
        self.file_name = None

    def get_file(self, name):
        self.file_name = name

    def open_file(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.char_stats:
                            self.char_stats[char] += 1
                        else:
                            self.char_stats[char] = 0

    def sort_dict(self):
        total = sum(self.char_stats.values())
        result = sorted(self.char_stats.items(), key=lambda x: x[1], reverse=True)
        result.append(('Итого', total))
        return result


chars = Charstats()
chars.get_file("Война и мир.txt")
chars.open_file()

print(tabulate(chars.sort_dict(), headers=['Буква', 'Частота'], tablefmt="psql", stralign='center'))

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
