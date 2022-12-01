import random

GUESS_NUMBER = int()
_RESULT = {'bulls': 0, 'cows': 0}

def get_number():
    global GUESS_NUMBER
    GUESS_NUMBER = int("".join(random.sample("1234567890", 4)))
    if GUESS_NUMBER < 1000:
        GUESS_NUMBER = GUESS_NUMBER * 10
    GUESS_NUMBER = str(GUESS_NUMBER)
    return GUESS_NUMBER

def check_number(num):
    global _RESULT
    bulls = 0
    cows = 0
    for i in range(len(num)):
        if num[i] == GUESS_NUMBER[i]:
            bulls += 1
        for y in range(len(GUESS_NUMBER)):
            if num[i] == GUESS_NUMBER[y] and num[i] != GUESS_NUMBER[i]:
                cows += 1
    _RESULT['bulls'] = bulls
    _RESULT['cows'] = cows
    return _RESULT
