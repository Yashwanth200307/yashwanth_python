'''
Created on 15-May-2025

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
driver.get('https://testautomationpractice.blogspot.com/')

''' 3 enter name , phone, email '''
name_txt_bx = driver.find_element(By.ID, 'name')
name_txt_bx.send_keys("Vivek")

email_txt_bx = driver.find_element(By.ID, 'email')
email_txt_bx.send_keys("123@gmail.com")

phone_txt_bx = driver.find_element(By.ID, 'phone')
phone_txt_bx.send_keys("1234567810")

# --- Address ---
address_txt_bx = driver.find_element(By.ID, 'textarea')
address_txt_bx.send_keys("123 Main Street, Mysuru, India - 570001")

# --- Radio Button ---
male_radio_btn = driver.find_element(By.ID, 'male')
male_radio_btn.click()


#--- check box ---
thursday_chk_box = driver.find_element(By.ID, 'thursday')
thursday_chk_box.click()

#--- Same ---
sunday_chk_box = driver.find_element(By.ID, 'sunday')
sunday_chk_box.click()

# --- dropbox ---
country_chk_box = driver.find_element(By.ID, 'country')
country_chk_box.click()

option_india = driver.find_element(By.XPATH, "//option[text()='India']")
option_india.click()

# #dropbox
# country_chk_box = driver.find_element(By.ID, 'country')
# country_dropdown = select(country_chk_box)
# country_dropdown.select_by_visible_text("India")


