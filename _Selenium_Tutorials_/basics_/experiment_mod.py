'''
Created on 24-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains
from time import sleep



'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''ActionsChains class and objects'''

actions = ActionChains(driver)

'''drag and drop'''
actions.scroll_by_amount(0, 550).perform()
source = driver.find_element(By.XPATH, '//*[@id="draggable"]')

target = driver.find_element(By.XPATH, '//*[@id="droppable"]')

actions.drag_and_drop(source,target).perform()

time.sleep(2)


'''drag and drop reverse'''

# Locate source and target
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")


# (reverse)
actions.drag_and_drop_by_offset(source, -140, 0).perform()
