'''
Created on 29-Apr-2025

@author: User1
'''
'''
#if a number is even or odd  1 

num = int(input("Please enter a number: "))

if num % 2 == 0:
    print(f"The number {num} is Even.")
else:
    print(f"The number {num} is Odd.")

print(":)")

'''
'''
#largest of two   2
a = 5
b = 8

if a > b:
    print(f"{a} is larger than {b}")
else:
    print(f"{b} is larger than {a}")
'''    
    

#voter age 3
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet 😒.")

'''
#largest of three   4

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is 🫡:", largest)
'''
'''
# finding leap year  5
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year 👍")
else:
    print(f"{year} is not a leap year 👎.")
'''