# the following program creates dice simulator using a function
import random

def random_number(max_int):
    print("rolling the dice ")
    rand_num = (random.randint(a=1, b=max_int))
    return rand_num

a_number = random_number(100)
print(a_number)

def random_number(max_int):
    print("rolling the dice ")
    rand_num = (random.randint(a=1, b=max_int))
    return rand_num

a_number = random_number(50)
print(a_number)

print("ur result is: ")
if (a_number + a_number) <=50:
    print(a_number + a_number)
elif(a_number + a_number) >=51:
    print("error")







