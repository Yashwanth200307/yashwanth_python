'''
Created on 31-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys

'''chrome options'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)



'''navigating to chrome'''

driver.get("https://testautomationpractice.blogspot.com/?m=1")


row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
rows_count = len(row_list)
# print("rows count:😎" ,rows_count)

column_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td')
columns_count = len(column_list)
# print("columns count😎", columns_count)


row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
rows_count = len(row_list)

# print("Book Names:")

name = input("Enter book name: ")

for j in range(2, rows_count + 1):
    book_name = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[1]')
    book_name = book_name.text
    # print(book_name)
    price = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[4]')
    price = price.text
    # print(price)
        


    if book_name == name:
        print("Price of", book_name, "is", price)
        break
else:
    print("Book not found.")





