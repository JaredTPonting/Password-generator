import random
import string
from random import randint


upper = string.ascii_letters[26:]
lower = string.ascii_letters[0:26]


def genPass(leng):
    password = ''
    for i in range(leng):
        dec = random.randint(0,2)
        if dec == 1:
            password = password + str(upper[random.randint(0,25)])
        elif dec == 2:
            password = password + str(lower[random.randint(0,25)])
        else:
            password = password + str(random.randint(0,9))
    print(password)
        
genPass(8)
