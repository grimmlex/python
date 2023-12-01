import collections
from math import factorial


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

text0112 = "TTTT"


def dna_to_rna(dna):
    return "".join(["U" if i == "T" else i for i in dna])

# #2
