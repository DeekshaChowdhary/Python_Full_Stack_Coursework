# ------------------------------ Encapsulation ------------------------------
'''
Encapsulation is one of the key principles of Object-Oriented Programming (OOP). It
bundles data (attributes) and methods (functions) into a single unit (class) while  
restricting direct access to some data to ensure security and maintainability.

Why Encapsulation?
● Data Security: Prevents unauthorized access to sensitive data.
● Code Maintainability: Reduces dependencies and improves modularity.
● Controlled Access: Allows validation and modification through methods.
● Data Integrity: Protects data from unintended modifications.

2. Types of Attributes in Encapsulation
Python allows three levels of access control for attributes:

1. Public (username): Can be accessed and modified from anywhere.

2. Protected (_otp): Meant for internal use within the class and subclasses but still
accessible.

3. Private (__password): Restricted access within the class only.

'''


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


#----------------------Examples-------------------------------------------

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
