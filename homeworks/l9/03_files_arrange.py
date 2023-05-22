# -*- coding: utf-8 -*-

import os, time, shutil
from pprint import pprint

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class SortFiles:
    def __init__(self, start_dir, new_dir):
        self.file_dict = {}
        self.start_dir = str(start_dir)
        self.new_dir = str(new_dir)
        os.makedirs(self.new_dir, exist_ok=True)
        self.start_dir_list = list(os.walk(self.start_dir))

        self.create_files_dict()
        self.make_dir()

    def create_files_dict(self):
        for i in self.start_dir_list:
            if i[2]:
                for y in i[2]:
                    normal_path = os.path.join(i[0], y)
                    self.file_dict[normal_path] = list(time.gmtime(os.path.getmtime(normal_path)))

    def make_dir(self):
        for keys, year in self.file_dict.items():
            if year[0] not in list(os.walk(self.new_dir))[0][1]:
                os.makedirs(f'{self.new_dir}/{year[0]}', exist_ok=True)
                new_path = f'{self.new_dir}/{year[0]}'
                if year[1] not in list(os.walk(new_path))[0][1]:
                    os.makedirs(f'{self.new_dir}/{year[0]}/{year[1]}', exist_ok=True)
                    shutil.copy2(keys, f'{self.new_dir}/{year[0]}/{year[1]}')


files = SortFiles(start_dir='icons', new_dir='icons_by_year')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
