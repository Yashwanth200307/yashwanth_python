'''
Created on 23-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)  
driver.implicitly_wait(10)


driver.get('https://testautomationpractice.blogspot.com/')


prompt_alert_btn = driver.find_element(By.XPATH, '//*[@id="promptBtn"]')
prompt_alert_btn.click()


prompt_alert = driver.switch_to.alert  
print(prompt_alert.text)

time.sleep(4)

prompt_alert.send_keys("Yashwanth")


prompt_alert.accept()
# confirmation_alert.dismiss()


