'''
Created on 10-May-2025

@author: User1

Inheritance: Carry forwarding properties from one class to another class.
** Inheritance is a mechanism where a new class ,inherits properties and
behaviors from an existing class


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
'''
object:-
* object class is supirior class 
* object class is a parent class of all class 
'''
'''
super():- class keyword is used to called superclass method and constructer to child class
when there is a constructor or method present in child class with same as super class
'''
'''
class GrandFather:
    def __init__(self, name):
        print("Object is created with name:", name)
        
    def gf_method(self):
        print("This is Grand father method")
        
class Mother(GrandFather): 
    
    def __init__(self):
        print("This is mother class constructor")
      
    def m_method(self):
        print("This is Mother method")
        
    def c_method(self):
        print("This is mother class c_method")
        
    def car(self):
        print("This is Mother's car")
        
class Father:
    def f_method(self):
        print("This is Father method")
        
    def car(self):
        print("This is Father's car")
        
class Child(Father, Mother):
'''
    # def __init__(self):
    #     print("This is child class constructor")
'''   
    def c_method(self):
        print("This is Child class c_method")

print("======GrandFather Object======")
ajja=GrandFather("ajja")
# ajja.gf_method()

print("======Mother Object======")
amma=Mother("amma")
# amma.m_method()
# amma.gf_method()
# amma.c_method()

print("=======Child Object======")
paapu=Child("paapu")
# paapu.c_method()
# paapu.gf_method()
# paapu.m_method()
# paapu.f_method()
# paapu.car()


print("=======Method Resolution Order(MRO)=======")
print(Child.mro())

print("=======Directory- dir()========")
print(dir(paapu))



'''

class GrandFather:
    def __init__(self, name):
        print("Object is created with name:", name)
        
    def gf_method(self):
        print("This is Grand father method")
        
class Mother(GrandFather): 
    
    def __init__(self, name, age):
        # print(f"Object is created with name: {name} and age: {age}")
        super().__init__(name)
        print(f"Age of {name} is {age}")
    
    def m_method(self):
        print("This is Mother method")
        
    def c_method(self):
        print("This is mother class c_method")
        
    def car(self):
        print("This is Mother's car")
        
class Father:
    def f_method(self):
        print("This is Father method")
        
    def car(self):
        print("This is Father's car")
        
class Child(Father, Mother):
    '''
    def __init__(self):
        print("This is child class constructor")
    '''   
    def c_method(self):
        print("This is Child class c_method")

print("======GrandFather Object======")
ajja=GrandFather("ajja")
# ajja.gf_method()

print("======Mother Object======")
amma=Mother("amma", 50)
# amma.m_method()
# amma.gf_method()
# amma.c_method()

print("=======Child Object======")
paapu=Child("paapu", 25)
# paapu.c_method()
# paapu.gf_method()
# paapu.m_method()
# paapu.f_method()
# paapu.car()


print("=======Method Resolution Order(MRO)=======")
print(Child.mro())

print("=======Directory- dir()========")
print(dir(paapu))

