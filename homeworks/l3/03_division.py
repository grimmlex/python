# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 39
result = 0
print(a%b)
while a > b:
    result = a/b
    result1 = b * int(result)
    result2 = a - result1
    a=0
# TODO здесь ваш код
print(result2)
