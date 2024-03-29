# -*- coding: utf-8 -*-
import logging
# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'



def log_errors(file_name):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            import logging

            root_logger = logging.getLogger()
            root_logger.setLevel(logging.WARNING)
            handler = logging.FileHandler(file_name, 'a', 'utf-8')
            handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
            root_logger.addHandler(handler)

            print('Начинаем')
            try:
                func(*args, **kwargs)
            except:
                logging.warning('WArnsk', exc_info=True)
                print('Записали ошибку')
            return

        return wrapper
    return actual_decorator

# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
# for line in lines:
#     try:
#         check_line(line)
#     except Exception as exc:
#         print(f'Invalid format: {exc}')
# perky(param=440)
#

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
@log_errors('function_errors.log')
def func(i):
    return i / 0


func(10)