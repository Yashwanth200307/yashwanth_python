'''
Created on 26-Apr-2025

@author: User1
'''
#square fill 
'''
for j in range(6):
    for i in range(6):
        print("*" , end=" ")
    print()
'''
#right half pyramid
'''
for j in range(1,6):
    for i in range(j):
        print("*" , end=" ")
    print()
    
'''
#reverse right half pyramid
'''    
for j in range(6, 0, -1):  
    for i in range(j):  
        print("*", end=" ")
    print() 
'''
'''
for j in range(5):
    for k in range(5-j):
        print(" " , end=" ")
    for i in range(j):
        print("*" , end=" ")
    print()
'''

#reverse half left 

for j in range(5 , 0, -1):
    for k in range(5-j):
        print(" " , end=" ")
    for i in range(j):
        print("*" , end=" ")
    print()
