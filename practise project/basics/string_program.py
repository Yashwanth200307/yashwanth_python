'''
Created on 27-Apr-2025

@author: User1
'''
name= input("enter any name")
#name="yashu" 
print(len(name))
index=-1
reverse_string=""
while index>-(len(name)+1):
    reverse_string=reverse_string+name[index]
    index=index-1
    
print(reverse_string)
    
