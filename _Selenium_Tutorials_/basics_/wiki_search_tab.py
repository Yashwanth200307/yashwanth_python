'''
Created on 21-May-2025

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

''' 3 wiki tab button '''
wiki_search_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
wiki_search_input.send_keys("Selenium")

wiki_search_btn = driver.find_element(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input')
wiki_search_btn.click()

# time.sleep(5)

wiki_search_result = driver.find_element(By.XPATH, '//*[@id="wikipedia-search-result-link"]/a')
wiki_search_result.click()


