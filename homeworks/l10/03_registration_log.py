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
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s')) # or whatever
root_logger.addHandler(handler)

FILE_NAME = 'registrations.txt'


class PredictionError(Exception):
    """Error occurred during prediction."""


class ValueError(PredictionError):
    pass

class NotNameError(PredictionError):
    pass

class NotEmailError(PredictionError):
   pass


class Check_email:
    def __init__(self, filename):
        self.filename = filename
        self.email_list = []

    def open_file(self):
        with open(self.filename, 'r', encoding='utf8') as file:
            for line in file:
                self.email_list.append(line.split(' '))

    def check_number_elem(self):
        for line in self.email_list:
            if not len(line) > 2:
                self.email_list.remove(line)
                logging.info(f'ValueError in {line}', stack_info=True)
                # raise ValueError(f"influence data in {line}")

    # def check_data(self):
    #     for line in self.email_list:
    #         if len(line) > 2:
    #             if line[0].isalpha():
    #                 if '@' and '.' in line[1]:
    #                     if 10 < int(line[2]) < 99:
    #                         self.correct_email_list.append(line)
    #     print(len(self.correct_email_list))


try:
    star = Check_email(FILE_NAME)
    star.open_file()
    print(len(star.email_list))
    star.check_number_elem()
    print(len(star.email_list))

except Exception as e:
    logging.error(f'Error {e}')

