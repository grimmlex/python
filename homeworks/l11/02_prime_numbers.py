# -*- coding: utf-8 -*-


class PrimeNumbers:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        prime_numbers = []
        for number in range(2, self.n + 1):
            for prime in prime_numbers:
                if number % prime == 0:
                    break
            else:
                prime_numbers.append(number)
        return iter(prime_numbers)


# prime_number_iterator = PrimeNumbers(n=10000)
#
# for number in prime_number_iterator:
#     print(number)

def prime_numbers_generator(n):
    primes = []
    for number in range(2, n + 1):
        for prime in primes:
            if number % prime == 0:
                break
        else:
            yield number
            primes.append(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def lucky_number_filter(n):
    num = str(n)
    if len(num) % 2:
        half_number = int(len(num) / 2)
        left_num = [int(digit) for digit in num[0:half_number]]
        right_num = [int(digit) for digit in num[half_number + 1:]]
        return True if sum(left_num) == sum(right_num) else False



def palyndrome_number_filter(n):
    num = str(n)
    res = ''.join(reversed(num))
    return True if res == num else False




def automorphic_filter(n):
    automorphic_number = n**2
    num = str(n)
    return True if num == str(automorphic_number)[len(num):] else False


prime_number_iterator = PrimeNumbers(n=10000)

fil = filter(palyndrome_number_filter, prime_numbers_generator(n=100000))
print(list(fil))