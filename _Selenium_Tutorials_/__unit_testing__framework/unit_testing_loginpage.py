'''
Created on 07-Jun-2025

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


    def test_navigation_to_login_page(self):
        # '''1. Launching the chrome browser'''     (Methods)
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(10)
        
        '''2 navigate the page'''
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        
        
        '''3 validate whether the navigation is successful '''
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        url_portionm= "auth/login"
        
        actual_url = driver.current_url  
        
        actual_url = driver.current_url        
        
        # self.assertEqual(actual_url, expected_url, "Navigstion is failed")
        
        ''' enter user name '''
        username_bx = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username_bx.send_keys("Admin")
         
         
        '''enter the password'''
        
        password_bx = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password_bx.send_keys("admin123")
        
        ''' click on the login btn'''
        
        login_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_btn.click()
        
        
    def test_navigation_to_login_page(self):
        # '''1. Launching the chrome browser'''     (Methods)
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(10)
        
        
        '''2 navigate the page'''
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        
        
        '''3 validate whether the navigation is successful '''
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        url_portionm= "auth/login"
        
        actual_url = driver.current_url  
        
        
        '''login failed'''
        expected_url_ = " dashboard/index"
        actual_url = driver.current_url
        

        
        
        
        self.assertIn(expected_url, actual_url, "Navigstion is failed")

        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()