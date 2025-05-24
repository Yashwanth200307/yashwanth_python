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

iframe_btn = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a")
iframe_btn.click()

'''switch to outer frame 1st '''

outer_frame = driver.find_element(By.XPATH , '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer_frame)
 
'''inner frame '''
inner_iframe = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_iframe)


# driver.switch_to.frame(12)


'''enter the text'''
input_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
input_txt_bx.send_keys("immadipulikeshi")


# # driver.switch_to.frame('Multiple') 
# driver.switch_to.frame('/html/body/section/div/div/iframe')


# driver.switch_to.parent_frame()
# print(driver.switch_to.frame)



