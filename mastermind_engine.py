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

def check_number(num):
    nums_bulls = 0
    nums_cows = 0
    print(num)
    print(GUESS_NUMBER)
    if int(num) == int(GUESS_NUMBER):
        print("Вы победили")
    for i in range(len(num)):
        if num[i] == GUESS_NUMBER[i]:
            nums_bulls += 1
        for y in range(len(GUESS_NUMBER)):
            if num[i] == GUESS_NUMBER[y]:
                nums_cows += 1
    _RESULT = {'bulls': nums_bulls, 'cows': nums_cows}
    return _RESULT
