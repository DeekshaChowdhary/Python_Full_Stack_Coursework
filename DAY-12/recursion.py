##---------------RECURSION-----------------------
'''
Recursion is when a function calls itself again and again to solve a problem.

def fun():
    if base_con:
        return
    fun()

-Base Case → stops recursion 
-Without base case → infinite loop


#Printing in order   
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)
O/P-
1
2
3
4
5
6
7
8
9
10

#Printing  in reverse order
def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)

O/P-
10
9
8
7
6
5
4
3
2
1


def display(s,i):
    if i==len(s):
        return
    print(s[i])
    display(s,i+1)
display("Python Programming",0)
O/p-
P
y
t
h
o
n
 
P
r
o
g
r
a
m
m
i
n
g


##Printing  in reverse order
def display(s,i):
    if i==len(s):
        return
    display(s,i+1)
    print(s[i])
display("Python Programming",0)
O/p-
g
n
i
m
m
a
r
g
o
r
P
 
n
o
h
t
y
P

def display(s,i):
    if i==len(s):
        return
    print(s[:i+1])
    display(s,i+1)
display("Python Programming",0)
O/p-
P
Py
Pyt
Pyth
Pytho
Python
Python 
Python P
Python Pr
Python Pro
Python Prog
Python Progr
Python Progra
Python Program
Python Programm
Python Programmi
Python Programmin
Python Programming


def display(s,i):
    if i<=0:
        return
    display(s,i-1)
    print(s*i)
display("abc",5)

#O/p-
abc
abcabc
abcabcabc
abcabcabcabc
abcabcabcabcabc


def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
display("abcdefg",0,3)
O/p-
abc
bcd
cde
def


def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
display("abcdefg",0,5)

O/p-
abcde
bcdef


def display(l,i,sum):
    if i==len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display([1,2,3,4,5,6,7,8],0,0))

O/p-
36


def display(l,i,sum):
    if i==len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display(['python','java','html','css','javascript','flask'],0,''))

O/p-
pythonjavahtmlcssjavascriptflask


#------------------int,float,str,list,tuple,set,dict----------------

This is about “Pass by value vs Pass by reference (object behavior)” in Python

> Simple Understanding
1. Immutable Types
int, float, str, tuple

-Changes inside function DO NOT affect outside value

 2.Mutable Types 
list, dict, set

-Changes inside function DO affect outside value
------------------------------------------------------------------------
def display(n):
    n= n+10
    print("Inside:",n)
n=4
display(n)
print("Outside:", n)


def display(n):
    n=n+10
    print("Inside:",n)
n=10.3
display(n)
print("Outside:", n)


def display(n):
    n= n+ "lang"
    print("Inside:",n)
n='python'
display(n)
print("Outside:", n)


def display(n):
    n= n+[5,6]
    print("Inside:",n)
n=[1,2,3,4]
display(n)
print("Outside:", n)

def display(n):
    n= n+5,6)
    print("Inside:",n)
n=(1,2,3,4)
display(n)
print("Outside:", n)


def display(n):
    n["c"] = 3   # adding new key-value
    print("Inside:", n)

n = {"a": 1, "b": 2}
display(n)
print("Outside:", n)


def display(s):
    s.add(5)   # adding element
    print("Inside:", s)

s = {1, 2, 3, 4}
display(s)
print("Outside:", s)

'''






















