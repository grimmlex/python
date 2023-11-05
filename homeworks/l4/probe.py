input_str = [2, 4, 2, 6, 2, 8]

import math
from fractions import Fraction

def convert_fracts(lst):
    denominators = []
    numerators = []
    fracts = {}
    if isinstance(lst, str):
        lst = lst.split(',')

    for i in range(0, len(lst)):
        if i % 2 != 0:
            denominators.append(lst[i])
        else:
            numerators.append(lst[i])

    fracts = dict(zip(numerators, denominators))
    print(fracts)


print(math.gcd(2,3,4))
convert_fracts(input_str)
