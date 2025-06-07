'''
Created on 31-May-2025

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

'''dynamic web table'''

explorer_name = input("Enter name: ")


row_list = driver.find_elements(By.XPATH, '//*[@id="rows"]/tr')
rows_count = len(row_list)

'''Note always check the xpath'''

for j in range(1, rows_count + 1):
    name_1 = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]')
    name_1 = name_1.text
    memory = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]/following-sibling::td[contains(text(),"MB") and not(contains(text(),"/s"))]')
    memory = memory.text
    cpu_1 = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]/following-sibling::td[contains(text(), "%") and not (contains(text(),"MB"))]')
    cpu_1 = cpu_1.text
    Network_1 = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]/following-sibling::td[contains(text(), "Mbps") and not (contains(text(),"MB"))]')
    Network_1 = Network_1.text
    
    
    if name_1 == explorer_name:
        print("Memory of:-", name_1, "is", memory, "and CPU is ",cpu_1, "NETWORK is", Network_1, "Thank You" )
        break
else:
    print("No Memory (or) Not Found .")
    
    
