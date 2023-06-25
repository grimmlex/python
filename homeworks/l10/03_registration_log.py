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
import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
handler = logging.FileHandler('registrations_bad.log', 'w', 'utf-8')
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))  # or whatever
root_logger.addHandler(handler)

FILE_NAME = 'registrations.txt'


class PredictionError(Exception):
    """Error occurred during prediction."""


class MyValueError(PredictionError):
    pass


class EightError(MyValueError):
    pass


class NotNameError(PredictionError):
    pass


class NotEmailError(PredictionError):
    pass


class CheckEmail:
    def __init__(self):
        self.email_list = []

    def open_file(self, filename):
        with open(filename, 'r', encoding='utf8') as file:
            for line in file:
                self.email_list.append(line.split(' '))

    def check_number_elem(self, line):
        if not len(line) > 2:
            self.email_list.remove(line)
            raise MyValueError(f'Заполнены не все три поля, в строке - {line}')

    def check_name_isalpha(self, line):
        if not line[0].isalpha():
            self.email_list.remove(line)
            raise NotNameError(f'Имя содержит не только буквы, в строке - {line}')

    def check_email(self, line):
        if not ('@' and '.') in line[1]:
            self.email_list.remove(line)
            raise NotEmailError(f'Не верный email, в строке - {line}')

    def check_eight(self, line):
        if not (10 < int(line[2]) < 99):
            self.email_list.remove(line)
            raise EightError(f'Не верный возраст, в строке - {line}')

    def lets_go(self, filename):
        self.open_file(filename)
        for line in warn.email_list:
            try:
                warn.check_number_elem(line)
                warn.check_name_isalpha(line)
                warn.check_email(line)
                warn.check_eight(line)
            except EightError:
                logging.info(f'Не верный возраст- {line}', stack_info=False)
            except MyValueError:
                logging.info(f'Не все три элемента в строке - {line}', stack_info=False)
                # print(f"{e}")
            except NotNameError:
                logging.info(f'В имени не только буквы- {line}', stack_info=False)
                # print(f"{e1}")
            except NotEmailError:
                logging.info(f'Не верный емайл- {line}', stack_info=False)
                # print(f"{e1}")


warn = CheckEmail()
warn.lets_go(FILE_NAME)
