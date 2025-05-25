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

'''3. Wiki search'''
wiki_search_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
wiki_search_input.send_keys("Selenium")

wiki_search_btn = driver.find_element(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input')
wiki_search_btn.click()

time.sleep(20)

wiki_search_result = driver.find_element(By.XPATH, '//*[@id="wikipedia-search-result-link"]/a)[1]')
wiki_search_result.click()

'''
current_page_title = driver.title
print(current_page_title)

current_window = driver.current_window_handle


print(current_window)
driver.switch_to.new_window('tab') # It opens new tab/ window
'''
window_handles_list = driver.window_handles
# print(window_handles_list)

driver.switch_to.window(window_handles_list[1])

'''
new_window = driver.current_window_handle
print(new_window)

new_page_title = driver.title
print(new_page_title)
'''
history_link = driver.find_element(By.XPATH, '//*[@id="toc-History"]/a/div/span[2]')
history_link.click()

