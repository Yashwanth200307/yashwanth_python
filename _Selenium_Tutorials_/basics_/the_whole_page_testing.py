'''
Created on 21-May-2025

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
driver.implicitly_wait(10)



'''2 navigate the practice page'''
driver.get('https://testautomationpractice.blogspot.com/')

'''ActionsChains class and objects'''

actions = ActionChains(driver)

''' 3 enter name , phone, email '''
name_txt_bx = driver.find_element(By.ID, 'name')
name_txt_bx.send_keys("raju bhai ")

email_txt_bx = driver.find_element(By.ID, 'email')
email_txt_bx.send_keys("123@gmail.com")

phone_txt_bx = driver.find_element(By.ID, 'phone')
phone_txt_bx.send_keys("1234567810")

'''' Address '''
address_txt_bx = driver.find_element(By.ID, 'textarea')
address_txt_bx.send_keys("123 Main Street, Mysuru, India - 570001")


''' Radio Button '''
male_radio_btn = driver.find_element(By.ID, 'male')
male_radio_btn.click()


''' check box '''
thursday_chk_box = driver.find_element(By.ID, 'thursday')
thursday_chk_box.click()

''' Same '''
sunday_chk_box = driver.find_element(By.ID, 'sunday')
sunday_chk_box.click()

# --- only dropbox check ---
# country_chk_box = driver.find_element(By.ID, 'country')
# country_chk_box.click()

# #dropbox
# country_chk_box = driver.find_element(By.ID, 'country')
# country_dropdown = select(country_chk_box)
# country_dropdown.select_by_visible_text("India")


''' dropbox country selection '''
option_india = driver.find_element(By.XPATH, '//*[@id="country"]/option[10]')
option_india.click()


# ---- color selection ---
option_colors = driver.find_element(By.XPATH, '//*[@id="colors"]/option[7]')
option_colors.click()

''' animal selection '''
option_sortedlist = driver.find_element(By.XPATH, '//*[@id="animals"]/option[2]')
option_sortedlist.click()

''' date  picker 1 '''
date_picker = driver.find_element(By.ID, 'datepicker')
date_picker.send_keys("05/20/2025")

#--- date picker 2---
# name_txt_bx = driver.find_element(By.ID, 'txtDate')
# name_txt_bx.send_keys("21/07/2025")

# #--- date picker 2 ---
# name_txt_bx = driver.find_element(By.ID, 'txtDate')
# driver.execute_script("arguments[0].value = '21/07/2025';", name_txt_bx)


''' date picker 3 '''
start_date = driver.find_element(By.ID, "start-date")
end_date = driver.find_element(By.ID, "end-date")

start_date.send_keys("01-01-2024")
end_date.send_keys("01-02-2024")


submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
submit_btn.click()


''' Upload single file '''
single_file_input = driver.find_element(By.ID, 'singleFileInput')
single_file_input.send_keys('C:/Users/User1/OneDrive/Desktop/example.txt')

single_upload_btn = driver.find_element(By.XPATH, "//*[@id=\"singleFileForm\"]/button")
single_upload_btn.click()
  

'''- multiple file upload '''
multiple_file_input = driver.find_element(By.ID, 'multipleFilesInput')
multiple_file_input.send_keys('C:/Users/User1/OneDrive/Desktop/good mornings folks.txt')
multiple_file_input.send_keys('C:/Users/User1/OneDrive/Documents/new 1.txt')

multiple_upload_btn = driver.find_element(By.XPATH, "//*[@id=\"multipleFilesForm\"]/button")
multiple_upload_btn.click()

# ''' wiki tab button '''
# wiki_search_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
# wiki_search_input.send_keys("Selenium")
#
# wiki_search_btn = driver.find_element(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input')
# wiki_search_btn.click()
#
# # time.sleep(5)
#
# wiki_search_result = driver.find_element(By.XPATH, '//*[@id="wikipedia-search-result-link"]/a')
# wiki_search_result.click()


'''product table '''

productTable_chk_box = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[1]/td[4]/input')
productTable_chk_box.click()

pagination_btn = driver.find_element(By.XPATH, '//*[@id="pagination"]/li[2]/a')
pagination_btn.click()

productTable_chk_box = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[4]/td[4]/input')
productTable_chk_box.click()

productTable_chk_box = driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr[4]/td[4]/input')
productTable_chk_box.click()


'''Form section 1 '''
section1_txt_bx = driver.find_element(By.ID, 'input1')
section1_txt_bx.send_keys("Dakshinapatheshwara")

section1_btn = driver.find_element(By.XPATH, '//*[@id="btn1"]')
section1_btn.click()
  
'''section 2'''
section1_txt_bx = driver.find_element(By.ID, 'input2')
section1_txt_bx.send_keys("Immadi Pulikeshi")

section1_btn = driver.find_element(By.XPATH, '//*[@id="btn2"]')
section1_btn.click()

'''section 3'''
section1_txt_bx = driver.find_element(By.ID, 'input3')
section1_txt_bx.send_keys("Born on April 4, 618 AD")

section1_btn = driver.find_element(By.XPATH, '//*[@id="btn3"]')
section1_btn.click()

'''start and stop btn'''

start_btn = driver.find_element(By.XPATH, '//*[@id="HTML5"]/div[1]/button')
start_btn.click()


'''stop btn'''
stop_btn = driver.find_element(By.XPATH, '//*[@id="HTML5"]/div[1]/button')
stop_btn.click()


'''simple alert btn'''

simple_alert_btn = driver.find_element(By.XPATH, '//*[@id="alertBtn"]')
simple_alert_btn.click()

# switching to simple alert
simple_alert = driver.switch_to.alert

simple_alert_text = simple_alert.text
print(simple_alert_text)

time.sleep(4)

simple_alert.accept()


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

'''prompt btn'''

prompt_alert_btn = driver.find_element(By.XPATH, '//*[@id="promptBtn"]')
prompt_alert_btn.click()


prompt_alert = driver.switch_to.alert  
print(prompt_alert.text)

time.sleep(4)

prompt_alert.send_keys("Yashwanth")


prompt_alert.accept()


'''new tab opening btn'''
new_tab_alert_btn = driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button')
new_tab_alert_btn.click()


time.sleep(10)

window_handles_list = driver.window_handles

driver.switch_to.window(window_handles_list[0])

current_page_title = driver.title
print(current_page_title)

'''double click'''

double_click = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')

actions.double_click(double_click).perform()


'''slider drag right'''

slider_right = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')


actions.drag_and_drop_by_offset(slider_right, 60, 0).perform()

'''slider drag left'''
slider_left = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')


actions.drag_and_drop_by_offset(slider_left, -15, 0).perform()


'''combo block'''

combo_block_tab = driver.find_element(By.ID,'comboBox')
combo_block_tab.click()

select_item_tab = driver.find_element(By.XPATH,'//*[@id="dropdown"]/div[4]')
select_item_tab.click()



