# Mandy Ewing
#FizzBuzz
# Due 1-21-18
# Worked with Autumn


## calculates the multiples of 3 and Fizz
## calculates the multiples of 5 and Buzz
## if it is 15 should say FizzBuzz

import math


for x in range(1,101):
    if x % 3 == 0 and x % 5 ==0:
        print("FizzBuzz")
    elif x % 3==0:
        print("Fizz")
    elif x % 5==0:
        print("Buzz")
    else:
        print(x)

