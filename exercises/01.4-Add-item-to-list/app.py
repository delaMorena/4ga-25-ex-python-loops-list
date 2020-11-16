#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here
def get_random():
    for x in range(10):
        my_list.append(random.randint(0,100))
    return my_list
        

print(get_random())