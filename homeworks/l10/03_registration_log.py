# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

import os

FILE_NAME = 'registrations.txt'


class MyError(Exception):
    pass


class ValueError(MyError):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'ValueError, {self.message}'
        else:
            return 'ValueError has been raised'


class NotNameError(MyError):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NotNameError, {self.message}'
        else:
            return 'NotNameError has been raised'


class NotEmailError(MyError):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NotEmailError, {self.message}'
        else:
            return 'NotEmailError has been raised'


class Check_email:
    def __init__(self, filename):
        self.filename = filename
        self.email_list = []
        self.correct_email_list = []

    def open_file(self):
        with open(self.filename, 'r', encoding='utf8') as file:
            for line in file:
                self.email_list.append(line.split(' '))

    def check_number_elem(self, list):
        for line in list:
            pass
    def check_data(self):
        for line in self.email_list:
            if len(line) > 2:
                if line[0].isalpha():
                    if '@' and '.' in line[1]:
                        if 10 < int(line[2]) < 99:
                            self.correct_email_list.append(line)
        print(len(self.correct_email_list))



star = Check_email(FILE_NAME)
star.open_file()

