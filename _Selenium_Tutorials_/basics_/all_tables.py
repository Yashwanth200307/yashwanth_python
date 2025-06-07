'''
Created on 27-May-2025

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

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/?m=1")


actions = ActionChains(driver)
actions.scroll_by_amount(0, 600).perform()

'''product table '''



productTable_chk_box = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[1]/td[4]/input')
productTable_chk_box.click()

pagination2_btn = driver.find_element(By.XPATH, '//*[@id="pagination"]/li[2]/a')
pagination2_btn.click()

productTable_chk_box = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[4]/td[4]/input')
productTable_chk_box.click()

productTable_chk_box = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[3]/td[4]/input')
productTable_chk_box.click()


time.sleep(10)

