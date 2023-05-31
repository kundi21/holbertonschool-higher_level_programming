#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_n = int(repr(number)[-1])
if last_n > 5 and number > 0:
    print(f'Last digit of {number} is {last_n} and is greater than 5')
elif last_n == 0:
    print(f'Last digit of {number} is {last_n} and is 0')
elif last_n < 6 and number > 0:
    print(f'Last digit of {number} is {last_n} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is -{last_n} and is less than 6 and not 0')
