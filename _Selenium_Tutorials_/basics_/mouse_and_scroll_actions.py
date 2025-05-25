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

''' Navigating to practice site'''
# driver.get('https://demo.automationtesting.in/Frames.html')

driver.get('https://testautomationpractice.blogspot.com/')


'''ActionsChains class and objects'''


actions = ActionChains(driver)


'''scrolling '''

actions.scroll_by_amount(0, 1050).perform()

'''Mouse hover'''
point_me = driver.find_element(By.XPATH,'//*[@id="HTML3"]/div[1]/div/button')

actions.move_to_element(point_me).perform()


'''double click '''
double_click = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')

actions.double_click(double_click).perform()


'''drag and drop'''
actions.scroll_by_amount(0, 550).perform()
source = driver.find_element(By.XPATH, '//*[@id="draggable"]')

target = driver.find_element(By.XPATH, '//*[@id="droppable"]')

actions.drag_and_drop(source,target).perform()


'''another drag right'''

slider_right = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')


actions.drag_and_drop_by_offset(slider_right, 60, 0).perform()

'''drag left'''
slider_right = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')


actions.drag_and_drop_by_offset(slider_right, -15, 0).perform()

'''drag and drop original state'''

actions.scroll_by_amount(0, 550).perform()
source = driver.find_element(By.XPATH, '//*[@id="draggable"]')

target = driver.find_element(By.XPATH, '//*[@id="droppable"]')

actions.drag_and_drop(source, target)




