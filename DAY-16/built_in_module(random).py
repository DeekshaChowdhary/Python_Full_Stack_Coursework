#--------------------random Built-In Module----------------
'''
The random module is a built-in Python module used to generate random values and numbers.


import random
random.seed(7)

print(random.random()) ## randomly generate 0-1 number

print(random.randint(1,6)) ## generate int value between 1 to 6

print(random.uniform(1,6)) ## generate float value between 1 to 6

l = ['java','python','c','c++','html']

print(random.choice(l)) 
print(random.choices(l,k=2))


import random
l = [1,2,3,4]
random.shuffle(l)  ##shuffle the values
print(l)

'''
