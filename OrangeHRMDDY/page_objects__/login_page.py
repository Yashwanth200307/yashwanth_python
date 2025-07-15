from page_objects__.base_page_ import BasePage
from selenium.webdriver.common.by import By 

class LoginPage(BasePage):
    def __init__(self, driver):
        super.__init__(driver)
        self.username_locator = (By.NAME, "username")
        self.passsword_locator = (By.NAME, "password")
        self.login_btn_locator = (By.TAG_NAME, "button")
        
            
    def enter_username(self):
        self.enter_text(self.username_locator,)
    
    def enter_password(self):
        pass
    
    def click_login(self):
        pass
    
    
    