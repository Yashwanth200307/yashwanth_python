'''
Created on 02-Jun-2025

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

'''navigating to chrome'''
driver.get('https://testautomationpractice.blogspot.com/?m=1')

shadow_host = driver.find_element(By.CSS_SELECTOR, "#shadow_host")
  
'''Access the shadow root'''
shadow_root = shadow_host.shadow_root

''' the input field'''
input_field = shadow_root.find_element(By.CSS_SELECTOR, "input[type=text]:nth-child(5)")  

'''Send keys to input field'''
input_field.send_keys("Hello goode morno!")


'''shadow check box'''
shadow_chk_box = shadow_root.find_element(By.CSS_SELECTOR, "input[type=checkbox]:nth-child(7)")
shadow_chk_box.click()


'''shadow file upload'''
file_upload_input = shadow_root.find_element(By.CSS_SELECTOR, "input[type=file]:nth-child(9)")
file_upload_input.send_keys('C:\\Users\\User1\\OneDrive\\Desktop\\example.txt')

file_upload_box = shadow_root.find_element(By.CSS_SELECTOR, "input[type=file]:nth-child(9)")
# file_upload_box.click()



# shadow_text_field = driver.find_element(By.XPATH, '//*[@id="shadow_host"]//input[1]')
# shadow_text_field.send_keys("hello Good Morning")

# shadow_host = driver.find_element(By.CSS_SELECTOR, "#shadow_host")  
# '''Access the shadow root'''
# shadow_root = shadow_host.shadow_root
#
# '''Within the shadow root, find the input field'''
# input_field = shadow_root.find_element(By.CSS_SELECTOR, "input")  
#
# '''Send keys to the input field'''
# input_field.send_keys("Hello Shadow DOM!")


driver.execute_script(script)