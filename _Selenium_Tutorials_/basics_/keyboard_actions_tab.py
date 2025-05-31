'''
Created on 26-May-2025

@author: User1
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys

''' Launching the chrome browser'''

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)



''' Navigating to practice site'''

driver.get('https://testautomationpractice.blogspot.com/')


'''ActionsChains class and objects'''

actions = ActionChains(driver)

'''copying the text from field 1'''
'''control+A'''

field1_text_bx = driver.find_element(By.XPATH, '//*[@id="field1"]')
actions.key_down(Keys.CONTROL, field1_text_bx).send_keys('a').key_up(Keys.CONTROL).perform()


'''copying the text'''
'''control+C'''

# field1_text_bx = driver.find_element(By.XPATH, '//*[@id="field1"]')
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

'''pasting the text'''
'''control+V'''

field2_text_bx = driver.find_element(By.XPATH, '//*[@id="field2"]')

# field2_text_bx.click()

actions.key_down(Keys.CONTROL, field2_text_bx).send_keys('v').key_up(Keys.CONTROL).perform()


# '''intab switch'''
# lenovo_link = driver.find_element(By.XPATH, '//*[@id="lenovo"]')
# lenovo_link.click()
#
# time.sleep(5)
#
# actions = ActionChains(driver)
# actions.key_down(Keys.ALT).send_keys(Keys.ARROW_LEFT).key_up(Keys.ALT).perform()

name_txt_bx = driver.find_element(By.ID, 'name')
actions.key_down(Keys.SHIFT,name_txt_bx).send_keys("dont know").key_up(Keys.SHIFT).perform()
