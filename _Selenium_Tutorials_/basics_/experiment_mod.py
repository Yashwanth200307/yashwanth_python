'''
Created on 24-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')


lenovo_search_tab = driver.find_element(By.ID, 'lenovo')
lenovo_search_tab.click()

time.sleep(10)

window_handles_list = driver.window_handles

driver.switch_to.window(window_handles_list[0])

current_page_title = driver.title
print(current_page_title)