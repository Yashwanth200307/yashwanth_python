'''
Created on 25-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains


''' Launching the chrome browser'''

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)


'''object creation'''
actions = ActionChains(driver)


''' Navigating to practice site'''
driver.get('https://demo.guru99.com/test/simple_context_menu.html')

'''right clicking'''
right_click_me_btn = driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
actions.context_click(right_click_me_btn).perform()

time.sleep(4)

left_click_on_body = driver.find_element(By.XPATH, '//*[@id="authentication"]')
left_click_on_body.click()


time.sleep(4)

'''double click '''
double_click_me_to_see = driver.find_element(By.XPATH,'//*[@id="authentication"]/button')

actions.double_click(double_click_me_to_see).perform()

simple_alert = driver.switch_to.alert

time.sleep(4)
simple_alert.accept()


