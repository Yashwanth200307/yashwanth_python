from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __int__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)
        
    
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)      
        
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()    
        
    def get_current_url(self, locator):
        get_current_url = self.driver.current_url()
        return get_current_url 
    def validate_page(self,locator):
        
          