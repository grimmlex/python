# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

from os import scandir
from functools import wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        run_time = perf_counter() - start_time
        print(f'Функция {func} отработала {run_time : 0.4f} секунды')
        return result
    return _wrapper


class TradesVolatility:

    def __init__(self, path):
        self.files_path = path
        self.files_dict = {}
        self.volatility_dict = {}
        self.max_volatility_dict = {}
        self.zero_volatility_list = []
        self.min_volatility_dict = {}
        self.volatility_dict_sorted = {}

    def get_files(self):
        self.files_dict = {i.name: i.path for i in scandir(self.files_path)}

    def open_files(self):
        for i in self.files_dict.items():
            with open(i[1], 'r', encoding='cp1251') as file:
                self.get_volatility(file)

    def get_volatility(self, file):
        res = []
        res1 = []
        for line in file:
            res1 = line.split(',')
            if not res1[2].isalpha():
                res.append(float(res1[2]))

        max_cost = max(res)
        min_cost = min(res)
        average_price = (max_cost + min_cost) / 2
        volatility = ((max_cost - min_cost) / average_price) * 100

        self.volatility_dict[res1[0]] = volatility
        self.volatility_dict_sorted = dict(sorted(self.volatility_dict.items(), key=lambda item: item[1]))

    def get_zero_volatility(self):
        for k, y in self.volatility_dict_sorted.items():
            if y == 0 or y == 0.0:
                self.zero_volatility_list.append(k)

    def get_3min_volatility(self):
        for k, y in self.volatility_dict_sorted.items():
            if len(self.min_volatility_dict) > 2:
                return
            if y > 0:
                self.min_volatility_dict[k] = y

    def get_3max_volatility(self):
        reverse_dict = dict(sorted(self.volatility_dict.items(), key=lambda item: item[1], reverse=True))
        for k, y in reverse_dict.items():
            if len(self.max_volatility_dict) > 2:
                return
            self.max_volatility_dict[k] = y

    def print_result(self):
        print('Максимальная волатильность:')
        for i in self.max_volatility_dict.items():
            print(f'{i[0]} - {round(i[1], 2)} %')
        print('Минимальная волатильность:')
        for i in self.min_volatility_dict.items():
            print(f'{i[0]} - {round(i[1], 2)} %')
        print('Нулевая волатильность:')
        print(', '.join(self.zero_volatility_list))

    @timer
    def run(self):
        self.get_files()
        self.open_files()
        self.get_zero_volatility()
        self.get_3min_volatility()
        self.get_3max_volatility()
        self.print_result()


file_path = 'trades'
lan = TradesVolatility(file_path)
lan.run()
