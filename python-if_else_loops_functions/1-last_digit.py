#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
n = int(repr(number)[-1])

if n > 5 and number > 0:
    print(f'Last digit of {number} is {n} and is greater than 5')
elif n == 0:
    print(f'Last digit of {number} is {n} and is 0')
elif n < 6 and number > 0:
    print(f'Last digit of {number} is {n} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {-abs(n)} and is less than 6 and not 0')