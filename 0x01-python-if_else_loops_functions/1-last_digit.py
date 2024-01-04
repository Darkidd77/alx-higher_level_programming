#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lsdig = abs(number) % 10
if number < 0:
    lsdig = -(lsdig)
print(f"last digit of {number:d} is {lsdig:d} and is ", end="")

if lsdig == 0:
    print("0")
elif lsdig > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
