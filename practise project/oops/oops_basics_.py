'''
Created on 04-May-2025

@author: Yashwanth 
'''
'''
Methods are functions which are defined inside a class we can call methods using the objects of that class  

* method of one class can be using an object of that class..
what is constructor(__init__) it is a magic method used to construct an object by 
initialize specific values being while creating the object 
'''
'''
class Humanbeings():
    def walk(self):
        print("iam walking")
        print("i am eating")
        
obj1=Humanbeings()
obj1.walk()
'''
#print(type(obj1)) #<class '__main__.Humanbeings'>
#types give wich type if variable that belongs to 

class Humanbeings():
    def __init__(self, name):
        self.name=name
    
    def walk(self):
        print(f"{self.name} need to walk")
        print(f"{self.name} need to eat")
        
obj1=Humanbeings("Yashwanth")
obj1.walk()