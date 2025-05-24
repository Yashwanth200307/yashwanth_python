'''
Created on 24-May-2025

@author: User1
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By 


'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

'''2 navigate the practice page'''
driver.get('https://demo.automationtesting.in/Frames.html')

'''iframe switching'''

# driver.switch_to.frame('SingleFrame') #you can check with name , id and webelements
#
#
#
# '''enter anythihng'''
# input_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
# input_txt_bx.send_keys("Raju Bhai ")

driver.switch_to.frame('/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a')

driver.switch_to.parent_frame()

driver.switch_to.frame(13)
print(driver.switch_to.frame)



input_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
input_txt_bx.send_keys("Raju Bhai ")





