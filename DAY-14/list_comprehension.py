##-------------------------LIST COMPREHENSION------------------------------
'''
List comprehension is a short and easy way to create a list in one line
-Basic syntax
[expression for item in iterable]


a=[]
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)    -> hard, so list comprehension is used

---------------------------------------------------------------------------------

l=[i for i in range(1,11)]
print(l)
O/p-[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l=[i for i in range(1,100)]
print(l)
O/p-[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


l=[i for i in range(3,99,3)]
print(l)
O/p-[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96]


l=[i for i in range(1,100) if i%2==0]
print(l)
O/p-[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


l=[i*i for i in range(1,10)]
print(l)
O/p-[1,4,9,16,25,36,49,64,81]

l=[i*i*i for i in range(1,10)]
print(l)
O/p-[1, 8, 27, 64, 125, 216, 343, 512, 729]

##appending vowels

s='python programming'
vol='aeiouAEIOU'
l=[i for i in s if i in vol]
print(l)


s='python programming'
vol='aeiouAEIOU'
l=['*' for i in s if i in vol]
print(l)


s='python programming'
vol='aeiouAEIOU'
l=['*' if i in vol else i for i in s]
print(l)
O/p-
['p', 'y', 't', 'h', '*', 'n', ' ', 'p', 'r', '*', 'g', 'r', '*', 'm', 'm', '*', 'n', 'g']


l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
s=[0 if i%2==0  else i for i in l]
print(s)
O/P-
[7, 3, 0, 5, 1, 5, 0, 0, 1, 0, 0, 5, 0, 7, 3, 0]


l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
s={0 if i%2==0  else i for i in l}
print(s)
O/p-
{0, 1, 3, 5, 7}


l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
s={i: l.count(i) for i in l}
print(s)
O/p-
{7: 2, 3: 2, 2: 2, 5: 3, 1: 2, 6: 2, 4: 1, 8: 2}


l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
s=tuple(0 if i%2==0  else i for i in l)
print(s)
O/p-
(7, 3, 0, 5, 1, 5, 0, 0, 1, 0, 0, 5, 0, 7, 3, 0)

'''
##--------------------GENERATOR------------------------------
'''
A generator is a special type of function that returns values one by one using yield,
instead of returning all at once.
 
🔹 Generator               vs           Normal Function

Uses yield	                       Uses return
Gives values one by one	               Gives all at once
Saves memory	                       Uses more memory
Can pause & resume	               Runs fully at once


def reels():
    r=['1..100','101..200','201..300','301..400','401..500','501..600']
    for i in r:
        yield i
scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
O/p-
1..100
101..200
201..300
301..400
401..500
'''
def display():
    yield "pfs-50"
    yield "pfs-48"
    yield "pfs-41"
    yield "pfs-31"
    yield "pfs-30"
    yield "pfs-22"
    yield "pfs-15"
leave= display()
for i in range(7):
    print(next(leave))
O/p-
pfs-50
pfs-48
pfs-41
pfs-31
pfs-30
pfs-22
pfs-15
















    


















    


















    


















    

















    



















    



















    
















