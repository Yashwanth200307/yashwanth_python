'''
Created on 03-Jun-2025

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
driver.implicitly_wait(10)



'''2 navigate the practice page'''
driver.get('https://testautomationpractice.blogspot.com/')

'''ActionsChains class and objects'''

actions = ActionChains(driver)


'''date picker 2 '''
driver.execute_script('document.getElementByID("txtDate").removeAttribute("readonly")')
date_picker2 = driver.find_element(By.ID, 'txtDate')
date_picker2.send_keys("03/06/2025")