import random


GUESS_NUMBER = int()
_RESULT = {}


def get_number():
    global GUESS_NUMBER
    GUESS_NUMBER = int("".join(random.sample("1234567890", 4)))
    if GUESS_NUMBER < 1000:
        GUESS_NUMBER = GUESS_NUMBER * 10
    GUESS_NUMBER = str(GUESS_NUMBER)
    return GUESS_NUMBER


get_number()
print(GUESS_NUMBER)


def check_number(num):
    if num == GUESS_NUMBER:
        print("Вы победили")
    bulls =
    nums_bulls = ""
    nums_cows = ""
    _RESULT = {'bulls': nums_bulls, 'cows': nums_cows}
    return _RESULT
check_number(GUESS_NUMBER)



