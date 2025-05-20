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
name_txt_bx.send_keys("raju bhai ")

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

# --- only dropbox check ---
# country_chk_box = driver.find_element(By.ID, 'country')
# country_chk_box.click()

# #dropbox
# country_chk_box = driver.find_element(By.ID, 'country')
# country_dropdown = select(country_chk_box)
# country_dropdown.select_by_visible_text("India")


#---- dropbox country selection ----
option_india = driver.find_element(By.XPATH, '//*[@id="country"]/option[10]')
option_india.click()


# ---- color selection ---
option_colors = driver.find_element(By.XPATH, '//*[@id="colors"]/option[7]')
option_colors.click()

# ---- animal selection ----
option_sortedlist = driver.find_element(By.XPATH, '//*[@id="animals"]/option[2]')
option_sortedlist.click()

#---- date  picker 1----
date_picker = driver.find_element(By.ID, 'datepicker')
date_picker.send_keys("05/20/2025")

#--- date picker 2---
# name_txt_bx = driver.find_element(By.ID, 'txtDate')
# name_txt_bx.send_keys("21/07/2025")

#--- date picker 2 ---
name_txt_bx = driver.find_element(By.ID, 'txtDate')
driver.execute_script("arguments[0].value = '21/07/2025';", name_txt_bx)


#----date picker 3---
start_date = driver.find_element(By.ID, "start-date")
end_date = driver.find_element(By.ID, "end-date")

start_date.send_keys("01-01-2024")
end_date.send_keys("01-02-2024")


submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
submit_btn.click()


''' Upload single file'''
single_file_input = driver.find_element(By.ID, 'singleFileInput')
single_file_input.send_keys('C:\\Users\\User1\\OneDrive\\Desktop\\example.txt')

single_upload_btn = driver.find_element(By.XPATH, "//*[@id=\"singleFileForm\"]/button")
single_upload_btn.click()


#---- multiple file upload---
multiple_file_input = driver.find_element(By.ID, 'multipleFilesInput')
multiple_file_input.send_keys('C:\\Users\\User1\\OneDrive\\Desktop\\good mornings folks.txt')
multiple_file_input.send_keys('C:\\Users\\User1\\OneDrive\\Documents\\new 1.txt')

multiple_upload_btn = driver.find_element(By.XPATH, "//*[@id=\"multipleFilesForm\"]/button")
multiple_upload_btn.click()