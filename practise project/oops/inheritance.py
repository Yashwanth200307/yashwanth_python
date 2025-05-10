'''
Created on 10-May-2025

@author: User1

Inheritance: Carry forwarding properties from one class to another class.

Parent/ Super class: From which class property is being inherited (Ex: HumanBeings class)  
Child/ sub class: To which class a property is being inherited (Ex: Male class, Female class)

How we can check? 

From object perspective, an object created from a child class should be able to access/ call the 
properties from its parent class

Why we need inheritance?
- It reduces code repetition and increase code reusability which helps us in easy maintanence

Types of inheritance:
1. Single level inheritance
2. Multi-level inheritance
3. Multiple inheritance
'''

class GrandFather:
    def gf_method(self):
        print("This is Grand father method")
        
class Mother(GrandFather): 
    def m_method(self):
        print("This is Mother method")
        
class Father:
    def f_method(self):
        print("This is Father method")
        
class Child(Mother, Father):
    def c_method(self):
        print("This is Child method")

print("======GrandFather Class======")
ajja=GrandFather()
ajja.gf_method()

print("======Mother Class======")
amma=Mother()
amma.m_method()
amma.gf_method()

print("=======Child Class======")
paapu=Child()
paapu.c_method()
paapu.gf_method()
paapu.m_method()
paapu.f_method()



