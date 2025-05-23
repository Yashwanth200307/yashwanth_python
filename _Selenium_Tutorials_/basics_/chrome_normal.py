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

'''2 navigate the practice page'''
driver.get('https://www.youtube.com/')


name_txt_bx = driver.find_element(By.ID, "ytSearchboxComponentInput yt-searchbox-input title")
name_txt_bx.send_keys("gta vice city ")


