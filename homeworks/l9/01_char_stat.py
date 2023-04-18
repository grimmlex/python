# -*- coding: utf-8 -*-

from tabulate import tabulate


class Charstat:
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
        result = sorted(self.char_stats.items(), key=lambda x: x[1], reverse=True)
        total = sum(self.char_stats.values())
        result.append('')
        result.append(('Итого', total))
        return result


chars = Charstat()
chars.get_file("Война и мир.txt")
chars.open_file()

print(tabulate(chars.sort_dict(), headers=['Буква', 'Частота'], tablefmt="psql", stralign='center', numalign='center'))

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
