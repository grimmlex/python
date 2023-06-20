# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint, choice
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

ENLIGHTENMENT_CARMA_LEVEL = 777
CARMA_LEVEL = 0

class IamGodError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'IamGodError, {self.message}'
        else:
            return 'IamGodError has been raised'


class DrunkError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'DrunkError, {self.message}'
        else:
            return 'DrunkError has been raised'


class CarCrashError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'CarCrashError, {self.message}'
        else:
            return 'CarCrashError has been raised'


class GluttonyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'GluttonyError, {self.message}'
        else:
            return 'GluttonyError has been raised'


class DepressionError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'DepressionError, {self.message}'
        else:
            return 'DepressionError has been raised'


class SuicideError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'SuicideError, {self.message}'
        else:
            return 'SuicideError has been raised'


my_error_list = [
    IamGodError,
    DrunkError,
    CarCrashError,
    GluttonyError,
    DepressionError,
    SuicideError,
]

error_stats_dict = {}


def one_day():
    global CARMA_LEVEL
    CARMA_LEVEL += randint(1, 7)
    if randint(1, 13) == 13:
        error_name = my_error_list[randint(0, 5)]
        if error_name in error_stats_dict:
            error_stats_dict[error_name] += 1
        else:
            error_stats_dict[error_name] = 1
        raise error_name
    return CARMA_LEVEL



while CARMA_LEVEL < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        print(one_day())
    except:
        print('Что-то случилось')
        logging.error("Error", exc_info=True)

