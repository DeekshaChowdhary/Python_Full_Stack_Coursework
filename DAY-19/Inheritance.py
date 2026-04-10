
#----------------------INHERITANCE-----------------------------------
'''

Inheritance is one of the core concepts in object-oriented programming. It allows a class
(called the child or subclass) to inherit properties and methods from another class
(called the parent or superclass).
This promotes code reuse, modularity, and makes it easier to maintain and scale
applications.


#single inheritance
class A:
class B(A):

#mutliple inheritance
class A:
class B:
class C(A,B):

#mutlilevel inheritance
class A:
class B(A):
class C(B):

#hierarical inheritance
class A:
class B(A):
class C(A):
class D(A):
'''

#single inheritance
class InstagramV1:
    def reel(self):
        print("You can post the reel")
class InstagramV2(InstagramV1):
    def story(self):
        print("You can upload a story")

print("d-instagramV1")
k=InstagramV1()
k.reel()
print("c-instagramV2")
k1=InstagramV2()
k1.reel()
k1.story()

#multilevel inheritance
class InstagramV1:
    def reel(self):
        print("You can post the reel")
class InstagramV2(InstagramV1):
    def story(self):
        print("You can upload a story")
class InstagramV3(InstagramV2):
    def note(self):
        print("You can add a note")
print("d-instagramV1")
k=InstagramV1()
k.reel()
print("c-instagramV2")
k1=InstagramV2()
k1.reel()
k1.story()
print("k-instagramV3")
k2=InstagramV3()
k2.reel()
k2.story()
k2.note()

#multiple inheritance
class InstagramV1:
    def reel(self):
        print("You can post the reel")
class InstagramV2(InstagramV1):
    def story(self):
        print("You can upload a story")
class InstagramV3(InstagramV2):
    def note(self):
        print("You can add a note")
class meta:
    def ai(self):
        print("you can use ai")
class crossplatform:
    def integrating(self):
        print("You can integrate with whatsapp and facebook")
class InstagramV4(meta,crossplatform,InstagramV3):
    def repost(self):
        print("You can repost the reel")
 


print("d-instagramV1")
k=InstagramV1()
k.reel()
print("c-instagramV2")
k1=InstagramV2()
k1.reel()
k1.story()
print("k-instagramV3")
k2=InstagramV3()
k2.reel()
k2.story()
k2.note()
print("k1-instagramV3")
k3=InstagramV4()
k3.ai()
k3.integrating()
k3.repost()
k3.reel()
k3.story()
k3.note()

#hierarical inheritance
class InstagramV1:
    def reel(self):
        print("You can post the reel")
class InstagramV2(InstagramV1):
    def story(self):
        print("You can upload a story")
class InstagramV3(InstagramV2):
    def note(self):
        print("You can add a note")
class meta(InstagramV3):
    def ai(self):
        print("you can use ai")
class crossplatform(InstagramV3):
    def integrating(self):
        print("You can integrate with whatsapp and facebook")
        

#method overriding--->super() method
'''
super() is a Python built-in function that returns a proxy object allowing
you to call methods from a parent or superclass without explicitly naming
it. It respects Python’s Method Resolution Order (MRO) and helps
avoid redundancy, making code cleaner and more maintainable.
'''

class WhatsappV0:
    def status(self):
        print("You can upload image and videos")
class WhatsappV1(WhatsappV0):
    def status(self):
        super().status()
        print("you can like,react and reply")
class WhatsappV2(WhatsappV1):
    def status(self):
        super().status()
        print("you can add music and filter")
k=WhatsappV2()
k.status()

#super() method for multiple inheritance
class WhatsappV0:
    def status(self):
        print("You can upload image and videos")
class WhatsappV1():
    def status(self):
        print("you can like,react and reply")
class WhatsappV2(WhatsappV0,WhatsappV1):
    def status(self):
        WhatsappV0.status(self)
        WhatsappV1.status(self)
        print("you can add music and filter")
k=WhatsappV2()
k.status()




