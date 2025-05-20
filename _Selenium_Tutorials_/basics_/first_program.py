'''
Created on 11-May-2025

@author: User1
'''
'''
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized") 

driver = webdriver.Chrome(options=options) 
driver.get('https://selenium.dev/')

time.sleep(30)
'''

'''
#Launching the chrome browser
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://selenium.dev/')
'''
'''
#optoions = webdriver.ChromeOptions() 

from selenium import webdriver




options = webdriver.ChromeOptions()
options.add_argument("start-maximized") #used for maxing the screen 

options.add_experimental_option("detach", True) #used to hold the screen
driver = webdriver.Chrome(options)

driver.get('https://selenium.dev/') #the chrome selenium
'''

from selenium import webdriver
# from selenium.webdriver import Chrome, Edge


'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.get('https://selenium.dev/')


''' fetching the practice site'''

