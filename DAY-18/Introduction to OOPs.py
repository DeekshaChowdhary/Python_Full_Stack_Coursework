'''
class Flipkart:
    # Class attribute
    discount = 10

    @classmethod
    def updateDiscount(cls, new_discount):
        cls.discount = new_discount

    @staticmethod
    def welcome():
        print('Welcome to Flipkart')

    def myorders(self, order_id):
        # Instance attribute
        self.order_id = order_id
        print(f"You have ordered product with id: {self.order_id}")

        
# class att, class meth, inst att, ints method,static => object
# class att, class meth, static => class
# Objects
a = Flipkart()
b = Flipkart()

# Correct method calls
a.myorders(1)
a.myorders(2)
b.myorders(1)
b.myorders(3)

print(a.discount)
print(Flipkart.discount)
a.myorders(1)
print(a.order_id)
a.updateDiscount(20)
a.myorders(2)
a.welcome()

Flipkart.updateDiscount(20)
Flipkart.welcome()
'''


#------------------------------Contructor--------------------------------
'''
It is a special method that comes automatically when object is called.
A constructor in Python is a special method called __init__() that is automatically executed when
an object of a class is created. Its main purpose is to initialize theobject’s data (attributes).
It helps assign values to instance variables at the time of object creation, so we don’t need to
set them manually every time. Constructors improve code readability and make object initialization easy and efficient.


class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print(f'Hello {self.username} , welcome to Instagram')
        
a = Instagram('a','@aa123')
b = Instagram('b','@bb123')
c = Instagram('c','@cc123')



# ------------------------------ Encapsulation ------------------------------

class Instagram:
    def __init__(self, username, password):
        self.username = username          # public
        self.__password = password        # private
        self._posts = []                  # protected

    # to access protected data using property
    @property
    def myposts(self):
        return self._posts

    @myposts.setter
    def myposts(self, postname):
        self._posts.append(postname)

    # to access private data using methods
    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password


# ------------------------------ Usage ------------------------------

# public access
a = Instagram('a', '@a123')
print("Before updating:", a.username)
a.username = 'b'
print("After updating:", a.username)

# private access
print("Before updating:", a.get_password())
a.set_password('@aaa123')
print("After updating:", a.get_password())

# protected access
print(a.myposts)
a.myposts = "sunset.png"
a.myposts = "beach.mp4"
print(a.myposts)


#--------------------------------------------------------

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        #print(self.title)
        #print(self.author)
        #print(self.price)

        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")
        
book1 = Book('life','James',180)
book2 = Book('Code','Robert',245)
book1.display()
book2.display()
'''
#-----------------------------------------------------------------

class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
        
    def calculate_annual_salary(self):
        return self.base_salary * 12

emp1 = Employee("Deeksha",450000)
print(emp1.name)
print(emp1.base_salary)
print(emp1.calculate_annual_salary())

#--------------------------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name =  name
        self.marks = marks
        
    def average_return(self):
        return average




















