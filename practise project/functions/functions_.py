'''
Created on 27-Apr-2025

@author: Yashwanth
'''
'''
function is a  block of reuseable code to perform a specific task 

types of code 
1. predefined > readily available in python
   -builtin functions 
2. userdefined>  created by programer 

why we need function
1. reduce repeatition of code/ reduce cpmplexity, minimize the no. of lines 
of code , this help in increased code readability 

sayntax

def function_name(parameteres):
<code>

def -> keywoord to define function 
function_name -> lower case separated by _ (manatory)
(): -> mandatory 


'''
'''
a = 2
b = 5
c= a+b
print(f"Sum of {a} and {b}:",c)

a = 6
b = 5
c= a+b
print(f"Sum of {a} and {b}:",c)
'''
'''

def welcome():
    print("hello world! hai")
    print("i hope yor're having a great day")
    
welcome()
welcome()

'''
'''
#multiplication
def multiplication(num,muliplier):
    result_mul=num*muliplier
    print(result_mul)
    
multiplication(d, 5)

'''
'''
#division 
def division_integer_division(dividend, divisor):
    div_quotient = dividend / divisor
    int_div_quotient = dividend // divisor
    return div_quotient, int_div_quotient

print(division_integer_division(7, 2))
'''
'''
#division 2
def division_integer_division(dividend, divisor):
    div_quotient = dividend / divisor
    int_div_quotient = dividend // divisor
    return div_quotient, int_div_quotient
div_output1, div_output2 = division_integer_division(7,2)
print(div_output1)
print(div_output2) 

'''

# f, g=5,6
# print(f)
# print(g)

#Function with parameters
def addition(a, b):
    c=a+b 
    # print(f"Addition of {a} and {b}:", c)
    return c
    
# d=addition(10, 20)
# print(d)

# print(addition(8, 10))
