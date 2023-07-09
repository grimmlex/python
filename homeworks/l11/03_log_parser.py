# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


from pyparsing import *


class Parser:

    def __init__(self, name, out_file):
        self.file_name = name
        self.dict = {}
        self.out_file_name = out_file

    def __iter__(self):
        if self.out_file_name is not None:
            out_file = open(self.out_file_name, 'w')
        else:
            out_file = None

        with open(self.file_name, 'r', encoding='cp1251') as file:
            if out_file:
                date = Word(nums + "- :")
                self_time = Word('.' + nums)
                word = Word('NOK')
                parse_module = (Suppress('[') + date + Suppress(self_time) + Suppress(']') + Suppress(word))(
                    'event_time')
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
        return iter(self.dict.items())


FILE_NAME = 'events.txt'
OUT_FILE_NAME = 'out.txt'


def parser_iterator(file_name, out_file_name):
    dict = {}
    if out_file_name is not None:
        out_file = open(out_file_name, 'w')
    else:
        out_file = None

    with open(file_name, 'r', encoding='cp1251') as file:
        if out_file:
            date = Word(nums + "- :")
            self_time = Word('.' + nums)
            word = Word('NOK')
            parse_module = (Suppress('[') + date + Suppress(self_time) + Suppress(']') + Suppress(word))(
                'event_time')
            result = OneOrMore(Group(parse_module))
            datafile = result.parseString(file.read()).asList()
            for item in datafile:
                if item[0][:-3] in dict:
                    dict[item[0][:-3]] += 1
                else:
                    dict[item[0][:-3]] = 1
            for key, value in dict.items():
                yield key, value
                out_file.write(str(f'{key} {value}\n'))
    if out_file:
        out_file.close()


grouped_events = parser_iterator('events.txt', 'out.txt')

for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')