import collections
from math import  factorial
def duplicate_encode(word):
    list_count = collections.Counter(word.lower()).most_common()
    result = []
    for i in word.lower():
        for y in range(0, len(list_count)):

            if i == list_count[y][0] and list_count[y][1] > 1:
                result.append(')')
                print('add')
            elif i == list_count[y][0] and list_count[y][1] == 1:
                result.append('(')

    return "".join(result)

# // ]]]21.11.2023

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
def decomp(n):
    arr = {}
    fact_number = factorial(n)
    if factorial(n) == 1:
        return 1
    for num in prime_numbers:
        decomp_division(fact_number, num)



def decomp_division(n, num):
    i = 1
    while True:
        number = n / num
        print(number)
        if number % num != 0:
            print('test')
            break
            return False
        else:
            i += 1
            continue
    return i

decomp(8)

print(5 % 2 != 0)