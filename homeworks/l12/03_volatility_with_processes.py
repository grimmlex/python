# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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


import multiprocessing
from os import scandir
from functools import wraps
from time import perf_counter, sleep
import queue


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
        self.files_dicts = []
        self.volatility_dict = {}
        self.list_keys = []
        self.list_values = []
        self.max_volatility_dict = {}
        self.zero_volatility_list = []
        self.min_volatility_dict = {}
        self.volatility_dict_sorted = {}

    def get_files(self):
        for i in scandir(self.files_path):
            self.files_dicts.append(i.path)
        return self.files_dicts

    def open_files(self, filelist, q_out: queue.Queue):
        for fil in filelist:
            with open(fil, 'r', encoding='cp1251') as file:
                self.get_volatility(file, q_out)

    @staticmethod
    def get_volatility(file, q_out: queue.Queue):
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
        q_out.put([res1[0], volatility])

    def create_global_volatility_dict(self, dt):
        self.volatility_dict[dt[0]] = dt[1]

    def sort_volatility_dict(self):
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

    def run(self):
        self.sort_volatility_dict()
        self.get_zero_volatility()
        self.get_3min_volatility()
        self.get_3max_volatility()
        self.print_result()

    @timer
    def main(self):
        self.get_files()
        ctx = multiprocessing.get_context('spawn')
        q_out = ctx.Queue()
        q1 = ctx.Queue()
        q1.put(self.get_files())

        length = len(self.files_dicts) / 2
        l1 = self.files_dicts[int(length):]
        l2 = self.files_dicts[:int(length)]

        proc1 = multiprocessing.Process(target=self.open_files, args=(l1, q_out,))
        proc2 = multiprocessing.Process(target=self.open_files, args=(l2, q_out,))

        proc1.start()
        proc2.start()
        try:
            for _ in range(len(self.files_dicts)):
                self.create_global_volatility_dict(q_out.get(timeout=1))
        except queue.Empty as err:
            print('Queue is empty')

        sleep(0.1)
        proc1.join()
        proc2.join()

        self.run()
        print(q1.get()[0])

file_path = 'trades'
lan = TradesVolatility(file_path)

if __name__ == "__main__":
    lan.main()
