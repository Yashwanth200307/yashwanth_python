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


'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

'''used for waiting'''
driver.implicitly_wait(10)


driver.get('https://testautomationpractice.blogspot.com/?m=1')


row_list = driver.find_elements(By.XPATH, '//*[@id="productTable"]/tbody/tr')
rows_count = len(row_list)

item_name = input("Enter a item Name:")


for j in range(1, rows_count + 1):
    item_name1 = driver.find_element(By.XPATH, f'//*[@id="productTable"]/tbody/tr[{j}]/td[2]')
    item_name1 = item_name1.text
    item_price = driver.find_element(By.XPATH, f'//*[@id="productTable"]/tbody/tr[{j}]/td[3]')
    item_price = item_price.text
    
    if item_name == item_name1:
        print("Price of ", item_name1, "Is", item_price)
        break
else:
    print("item not found (or) check the item")


# //*[@id="productTable"]/tbody/tr[4]
#
# //*[@id="productTable"]/tbody/tr[4]/td[1]