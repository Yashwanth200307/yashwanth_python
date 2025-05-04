'''
Created on 04-May-2025

@author: Yashwanth 
'''
'''
Methods are functions which are defined inside a class we can call methods using the objects of that class  

* method of one class can be using an object of that class..
'''
class Humanbeings():
    def walk(self):
        print("iam walking")
        print("i am eating")
        
obj1=Humanbeings()
obj1.walk()

#print(type(obj1)) #<class '__main__.Humanbeings'>
#types give wich type if variable that belongs to 

class Humanbeings():
    def __init__(self, name):
        pass
    def walk(self):
        print("iam walking")
        print("i am eating")
        
obj1=Humanbeings(Yashu)
obj1.walk()