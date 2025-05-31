'''
Created on 26-Apr-2025

@author: User1
'''
'''
day = int(input("Enter day number: "))

match day:
    case 1:
        print("Today is Sunday")
    case 2:
        print("Today is Monday")
    case 3:
        print("Today is Tuesday")
    case 4:
        print("Today is Wednesday")
    case 5:
        print("Today is Thursday")
    case 6:
        print("Today is Friday")
    case 7:
        print("Today is Saturday")
    case _:
        print("Invalid day number")
'''


#using if statment 
day = int(input("enter the day number:-"))
if day == 1:
    print("today is Sunday :)")
elif day==2:
    print("today is Monday :)")
elif day==3:
    print("today is Tuesday :)")
elif day==4:
    print("today is Wednesday :)")
elif day==5:
    print("today is Thursday :)")
elif day==6:
    print("today is Friday :)")
elif day==7:
    print("today is Saturday :)")
else:
    print("Invalid day Number :(")
    
