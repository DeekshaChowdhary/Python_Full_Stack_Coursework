#--------------------POLYMORPHISM--------------------------
'''
Polymorphism has same method but differnet actions
Types
1. Method Overloading - same method , different parameters, same/diff classes
2. Method Overridding - same method , same parameters , different actions , parent/child classes

Polymorphism means "many forms". In Python, it allows objects of different classes to be
treated as objects of a common superclass.

1. Method Overloading (Compile-Time Polymorphism)
Definition: Method overloading means having multiple methods with the same name
but different parameters.
 Note: Python doesn’t support traditional method overloading like Java or C++.
Instead, it uses default arguments or variable-length arguments to achieve similar
behavior.

2. Method Overriding (Run-Time Polymorphism)
 Definition: Method Overriding occurs when a subclass provides its own specific
implementation of a method that is already defined in its superclass. This is a key
feature of run-time polymorphism, allowing different behaviors based on the
object’s type at runtime..
 Real Use: This allows customizing inherited methods in child classes.


class Hotstar:
    def __init__(self,username):
        print(f"Hi {username}! \n Welcome to the hotstar!!!!")
    def promo(self):
        print("You can watch the promos")
    def login(self):
        print("You can login to the hotstar")
    def search(self):
        print("You can search the movies")
    def profiles(self):
        print("You can edit your profile")
    def videocontrollers(self):
        print("You can watch and play")
    def suggestions(self):
        print("You can check out the suggestions")

        
    def movie(self):
        print("You can access for old movies")
    def ads(self):
        print("Ads will run")
    def download(self):
        print("You can't download the movie")
    def quality(self):
        print("You can watch movie with low quality")

class PremiumHotstar(Hotstar):
    def __init__(self,username):
        print(f"Hi {username}! \n Welcome to the hotstar premium!!!!")
    def movie(self):
        print("You can access for all the movies")
    def ads(self):
        print("Ads won't run")
    def download(self):
        print("You can download the movie")
    def quality(self):
        print("You can watch movie with high quality")

a = Hotstar('Deeks')
a.promo()
a.login()
a.search()
a.profiles()
a.videocontrollers()
a.suggestions()
a.movie()
a.ads()
a.download()
a.quality()

print('\n')

a1 = PremiumHotstar('Deeks')
a1.movie()
a1.ads()
a1.download()
a1.quality()

'''

#----------------------Operator Overloading--------------------------
'''
Definition: Defining custom behavior for operators (+, -, *, etc.) when they are used
with user-defined objects.
 In Python: Special methods like __add__(), __sub__(), etc., are used.
'''

class number:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num + other.num
    def __sub__(self,other):
        return self.num - other.num
    def __mul__(self,other):
        return self.num * other.num
    def __truediv__(self,other):
        return self.num / other.num
    def __eq__(self,other):
        return self.num == other.num
    def __lt__(self,other):
        return self.num < other.num
    def __gt__(self,other):
        return self.num > other.num
    def __str__(self):
        return str(self.num)

a = number(10)
b = number(20)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a==b)
print(a>b)
print(a<b)
print(str)
    

























