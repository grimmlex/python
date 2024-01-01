import collections
from collections import defaultdict
from math import factorial
import re


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

from collections import defaultdict


def dec(n):
    decompres = defaultdict(lambda: 0)
    i = 2
    while n > 1:
        while n % i == 0:
            n /= i
            decompres[i] += 1
        i += 1
    return decompres


def decomp(n):
    answer = defaultdict(lambda: 0)
    for i in range(2, n + 1):
        for key, value in dec(i).items():
            answer[key] += value
    return ' * '.join(f'{x}^{y}' if y > 1 else str(x) for x, y in sorted(answer.items()))


# /// 01.12.2023
def find_dna(dna):
    return ["U" if i == "T" else i for i in dna]


# ???????????????2

text01121 = "aretheyhere"
text01122 = "yestheyarehere"


def longest(a1, a2):
   return "".join(sorted(set.union(set(a1), set(a2))))

#  09/12/2023
text091220231 = (1, 2, 3)


def maps(a):
    return [i * 2 for i in a]


# ????????????????????

def get_count(sentence):
    return len([i for i in sentence if i in "aeiouAEIOU"])


# ???????????????

def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce >= 1 or bounce <= 0 or window >= h:
        return -1
    count = 1
    jump_height = h * bounce
    while jump_height > window:
        jump_height *= bounce
        count += 2
    return count


# 16/12/2023
# 1
def find_it(seq):
    d = defaultdict(lambda: 0)
    for i in seq:
        d[i] += 1
    return [key for key, value in d.items() if value % 2 != 0][0]


# 2

def validate_pin(pin):
        return True if pin.isdecimal() and len(pin) in {4,6} else False


# 20\12\2023
def check_for_factor(base, factor):
    return True if base % factor == 0 else False

# 25.12.2023
