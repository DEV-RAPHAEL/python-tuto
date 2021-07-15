from  math import *
import random
level = 1
lives = 5
random = random.randint(1, 10)
number = int(input())
if number == random:
    print('Congrats')
    level+1
    print('Welcome to ', level)
elif number > random:
    print('Greater try again')
else:
     print('Lesser')