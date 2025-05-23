'''
Created on 23-May-2025

@author: User1
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By 


'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
import time


'''2 navigate the practice page'''
driver.get('https://testautomationpractice.blogspot.com/')

'''confirmation alert btn'''

confirmation_alert_btn = driver.find_element(By.XPATH, '//*[@id="confirmBtn"]')
confirmation_alert_btn.click()


# switching to simple alert
confirmation_alert = driver._switch_to.alert

confirmation_alert_text = confirmation_alert.text
print(confirmation_alert_text)

time.sleep(4)

# confirmation_alert.accept()
confirmation_alert.dismiss()

