'''
Created on 20-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
 
'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Upload single file'''
single_file_input = driver.find_element(By.ID, 'singleFileInput')
single_file_input.send_keys('C:\\Users\\User1\\OneDrive\\Desktop\\example.txt')

single_upload_btn = driver.find_element(By.XPATH, "//*[@id=\"singleFileForm\"]/button")
single_upload_btn.click()