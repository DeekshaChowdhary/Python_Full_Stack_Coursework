#------------------User-Defined Module---------------------------
Main.py 
'''
1-
import logic 
print(modules_logic.likes)
print(modules_logic.comments)
print(modules_logic.addlike())
print(modules_logic.addlike())
print(modules_logic.addcomments('Good'))

2-
import logic as ml
print(ml.likes)
print(ml.comments)
print(ml.addlike())
print(ml.addlike())
print(ml.addcomments('Good'))

3-
from logic import likes,comments,addlike,addcomments
print(likes)
print(comments)
print(addlike())
print(addlike())
print(addlike())
print(addcomments('Good'))


from logic import *
print(likes)
print(comments)
print(addlike())
print(addlike())
print(addlike())
print(addcomments('Good'))
'''

'''
#------------Calculator example(Main.py)--------------------

from logic import *

print(add(5,10))
print(sub(5,10))
print(mul(5,10))
print(div(5,10))
print(mod(5,10))


from logic import add,sub,mul,div,mod

print(add(5,10))
print(sub(5,10))
print(mul(5,10))
print(div(5,10))
print(mod(5,10))


import logic

print(logic.add(20,10))
print(logic.sub(20,10))
print(logic.mul(5,20))
print(logic.div(15,5))
print(logic.mod(25,10))


import logic as lg

print(lg.add(25,10))
print(lg.sub(25,10))
print(lg.mul(5,20))
print(lg.div(15,5))
print(lg.mod(25,10))

'''



