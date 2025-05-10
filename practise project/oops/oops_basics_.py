'''
Created on 04-May-2025

@author: Yashwanth 
'''
'''
Methods are functions which are defined inside a class.
We can call methods using the objects of that class.

A method of one class can be called using an object of that class.

Method Resolution Order(mro): 

Constructor(__init__): 

- It is a magic method used to construct an Object by initializing it with
specific values/ features being passed while creating the object.

- It is not mandatory to define a constructor. But when constructor is not defined interpretor 
will have its own constructor created

- Calling the constructor: 
    > Constructor is called implicitly during the creation of object
    > Still we can call constructor explicitly
    
Types of Variables:

1. Method variables/ local variables
2. Object variables/ instance variables
3. Class variables/ static variables

Major pillars/ concepts in OOPs:
1. Inheritance
2. Polymorphism
3. Abstraction
4. Encapsulation
'''

class HumanBeings():
    species="Sapiens"
    # genus="Homo"
    
    def __init__(self, name, age):
        self.name=name
        self.age= age
        HumanBeings.genus="Homo"
        print("This is constructor", name)
        
    def walk(self, hours):
        
        print(f"{self.name} is walking for {hours} hours")    
     
    def sleep(self, hours):   
        print(f"{self.name} is sleeping for {hours} hours")
        
    def display_scientific_name(self):
        print(f"{self.name} is {HumanBeings.genus} {HumanBeings.species}")

obj1=HumanBeings("Vivek", 32) 
obj1.walk(2)
obj1.sleep(8)
obj1.display_scientific_name()
# obj1.__init__("Sandeep", 35)

# print(type(obj1)) # <class '__main__.HumanBeings'>

obj2=HumanBeings("Yash", 22)
# obj2.walk()
# obj1.walk()
obj2.display_scientific_name()

# print(obj1.name)
# print(obj2.name)
#
# print(HumanBeings.mro())
# print(dir(obj1))

class Car:
    def move_forward(self):
        print("car is moving forward")
        
car1=Car()
# car1.move_forward()
# print(dir(car1))