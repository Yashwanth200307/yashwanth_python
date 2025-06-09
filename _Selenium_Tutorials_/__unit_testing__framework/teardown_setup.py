'''
Created on 08-Jun-2025

@author: User1
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys

class OrangeHRMLoginTest_(unittest.TestCase):



    def setUp(self):
        # '''1. Launching the chrome browser'''     (Methods)
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options)
        self.driver.implicitly_wait(10)
        
        '''2 navigate the page'''
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        # (it contains only two steps)

    def tearDown(self):
        self.driver.quit()
    
    
    
    def test_navigation_to_login_page(self):
        '''3 validate whether the navigation is successful '''
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        url_portionm= "auth/login"
        actual_url = self.driver.current_url 
        
        
        
        self.assertIn(expected_url, actual_url, "Navigstion is failed")
    
    def test_orangehrm_login(self):
        ''' enter user name '''
        username_bx = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username_bx.send_keys("Admin")
         
         
        '''enter the password'''
        
        password_bx = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password_bx.send_keys("admin123")
        
        ''' click on the login btn'''
        
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_btn.click()
        
        '''login failed'''
        expected_url_ = " dashboard/index"
        actual_url = self.driver.current_url
        
        # self.assertIn(expected_url, actual_url, "Navigstion is failed")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'OrangeHRMLoginTest.test_navigation_to_login_page']
    unittest.main()