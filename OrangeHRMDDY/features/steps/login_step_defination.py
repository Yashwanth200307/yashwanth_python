from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects__.base_page_ import BasePage
from page_objects__.login_page import LoginPage




@given(u'Chrome browser is launched')
def launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(options)
    # context.driver.implicitly_wait(10)  
    context.base_page = BasePage(context.driver)
    context.login_page = LoginPage(context.driver)     
    


@when(u'User navigates to OrangeHRM Login page')
def navigate_to_orangehrm_login_page(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@when(u'User enters username')
def enter_username(context):
    # username_bx = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    # username_bx.send_keys("Admin")
    context.login_page.enter_username("Admin")

@when(u'User enters password')
def enter_password(context):
    # password_bx = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    # password_bx.send_keys("admin123")
    
    context.login_page.enter_password("admin123")


@when(u'User clicks on login button')
def click_on_login_button(context):
    # login_btn = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    # login_btn.click()  
    
    context.login_page.click_login()      


@then(u'User should able to see dashboard/index in current page url')
def validate_dashboard_url(context):
    expected_url_member = "dashboard/index"
    actual_url = context.base_page.get_current_page_url()
    
    # context.assertIn(expected_url_member, actual_url, "Login failed")
    
    assert expected_url_member in actual_url, "Login failed"


@then(u'User should able to see auth/login in current page url')
def validate_login_page_url(context):
    expected_url_portion = "auth/login"
    actual_url = context.base_page.get_current_page_url()
    
    # context.assertIn(expected_url_portion, actual_url, "Navigation to OrangeHRM login page is failed")
    
    assert expected_url_portion in actual_url, "Navigation to OrangeHRM login page is failed"
    
@when(u'User enters username "{username}"')
def enter_username_parameter(context, username):
    # username_bx = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    # username_bx.send_keys(username)
    
    context.login_page.enter_username(username)

@when(u'User enters password "{password}"')
def enter_password_parameter(context, password):
    # password_bx = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    # password_bx.send_keys(password) 
    
    context.login_page.enter_password(password)

@then(u'User should able to see "{expected_url_member}" in current page url')
def validate_current_page_url(context, expected_url_member):
    expected_url_member = expected_url_member
    actual_url = context.base_page.get_current_page_url()
    print("actual_url-->", actual_url)
    assert expected_url_member in actual_url, "Expected URL is not present in Current page URL"
