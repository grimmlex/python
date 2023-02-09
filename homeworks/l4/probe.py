import simple_draw as sd

width = 1200
height = 800
sd.resolution = (width, height)

# Можно задать фоновое изображение. Нужно подключить библиотеку pygame и
# придется при каждой (или через двет-три) итерации  while перерисовывать фон
# раскомментировать строки 2, 13 и 56

# sd._background_image = pygame.image.load('001.jpg')

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 5


def start_point():
    x = height + 100
    y = sd.randint(10, width - 10)
    return sd.get_point(x, y)


def snowflake_gen():
    return {'length': sd.random_number(8, 24),
            'x': sd.randint(10, width - 10),
            'y': height + sd.randint(100, 150),
            'factor_a': sd.random_number(4, 7) / 10,
            'factor_b': sd.random_number(4, 7) / 10,
            'factor_c': sd.random_number(45, 60)
            }


snowflakes = []

for _ in range(N):
    snowflakes.append(snowflake_gen())
print(snowflakes)