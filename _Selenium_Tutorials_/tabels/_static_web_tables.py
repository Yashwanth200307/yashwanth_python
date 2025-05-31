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

book_name = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]')
book_name_text = book_name.text
print(book_name_text)


cell_22 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_text = cell_22.text
print(cell_22_text)


cell_23 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
cell_23_text = cell_23.text
print(cell_23_text)


price = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]')
price_text = price.text
print(price_text)
 

name = input("Enter book name: ")

for i in range(2, 6):
    book_name = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{i}]/td[1]').text
    price = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{i}]/td[4]').text

    if book_name == name:
        print("Price of", book_name, "is", price)
else:
    print("Book not found.")




# '''static tables'''
#
# book_name  = "Learn Selenium"
# book_price = driver.find_element(By.XPATH, f"//td[text()='{book_name}']/following-sibling::td[3]").text
# # print(price)
#
# print(book_price)




