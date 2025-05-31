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

'''clicking the switch btn'''
iframe_btn = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a")
iframe_btn.click()

'''switching To Outer frame 1st '''

outer_frame = driver.find_element(By.XPATH , '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer_frame)
 
''' Switching To Inner frame '''

inner_iframe = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_iframe)


'''Entering the text in box'''
input_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
input_txt_bx.send_keys("immadipulikeshi")
