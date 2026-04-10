##-----------------------User-Defined Modules-----------------------------
'''
A module in programming is simply a file that contains code (functions, variables, classes)
that you can reuse in other programs
-A file containing reusable code that can be imported and used in another program.


likes = 0
comments =[]
def addlike():
    global likes
    likes+=1
    return likes

def addcomments(com):
    comments.append(com)
    return comments

'''
#----------Calculator Example------------------------

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b
