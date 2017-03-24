import random

def rand7():
    return random.randint(1,7)


def rand5():
    number = 0

    while number not in [1, 2, 3, 4, 5]:
        number = rand7()

    return number

print(rand5())
