#---------------------------FUNCTIONS------------------------------

# syntax
def function_name(arg):
    #stmts
    return

function_name(para)


# function example:
def wish(name):
    print(f' Hello, {name} - welcome to codegnan')

wish('deeksha')
wish('sumalatha')


# four types of arguments

# **1.positional arguments**

def details(name, age):
    print("name: ", name)
    print("age: ", age)

details('deeksha', '20')
details('20', 'deeksha')


# **2.keyword arguments**

details(name='deeksha', age='20')
details(age='20', name='deeksha')


# **3.default argument**

def details(name, age, phone_no='+91'):
    print("name: ", name)
    print("age: ", age)
    print("phone_no:", phone_no)

details('deeksha', '20')
details('nani', '20', '876908')


# **4.variable length argument**

def display(*names):
    print("names:", names)

display('deeksha', 'nani', 'hima')
display('deeksha')


def display(**names):
    print("names:", names)

display(n1='deeksha', n2='nani', n3='hima')
display(n1='deeksha')

##Simple Calculator example

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a % b

exp = input("enter your expression: ")

if '+' in exp:
    a,b = exp.split('+')
    print(add(int(a),int(b)))

elif '-' in exp:
    a,b = exp.split('-')
    print(sub(int(a), int(b)))

elif '*' in exp:
    a,b = exp.split('*')
    print(mul(int(a), int(b)))

elif '/' in exp:
    a,b = exp.split('/')
    print(div(int(a), int(b)))

elif '%' in exp:
    a,b = exp.split('%')
    print(rem(int(a), int(b)))
