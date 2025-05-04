'''
Created on 02-May-2025

@author: User1
'''
'''
Argument = Parameters 

1. formal Arguments :- Parameters which are declared while defining a funciton  
2. Actual Arguments:-  actual valuves passed while calling a function

c=a+b
return c

d=addition(a,b): #a <b are formal Arguments
   c=a+b
   return c
'''
'''
def cal_energy(m, c= 300000000):
    e=m*c**2
    print("Energy in Joules:", e)
    
cal_energy(5, 5)
cal_energy(3)
'''


def addition(*a):
    print(a)
   
addition(1)
addition(1,4)
addition(1,5,6)
addition(1,5,7,4)


'''
#variable lent argument 
b =(3,4,5,6,7)
result=0
for num in b :
    result+=num
print(result) #it's store the output in the form of  "Tuple"

'''
'''
#keyword variable length argument
def display(**x):
    print(x)
    
display(name="Yashu", age="21", gender="male",Place="chitradurga") # it's store this output in "Dictionary" form
'''

