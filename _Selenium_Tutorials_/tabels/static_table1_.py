'''
Created on 29-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/?m=1")


row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
rows_count = len(row_list)
# print("rows count:😎" ,rows_count)

column_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td')
columns_count = len(column_list)
# print("columns count😎", columns_count)



name = input("Enter book name: ")



for j in range(2, rows_count+1):
    for i in range(1, columns_count+1):
        table_cell = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[{i}]')
        table_cell = table_cell.text
        print(table_cell)
        
        
        
#
#         if book_name.lower() == name.lower():
#             print("Price of", book_name, "is", price)
#             break
# else:
#     print("Book not found.")




'''
cell_22 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_text = cell_22.text
print(cell_22_text)


cell_23 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
cell_23_text = cell_23.text
# print(cell_23_text)

price = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th[4]')
price_text = price.text
print(price_text)
'''

book_name_1 = input("Enter book name---: ")

# if book_name_1 == "input":
#     print("Price of", book_name_1, "is", price)
# else:
#     print("Book not found.")

