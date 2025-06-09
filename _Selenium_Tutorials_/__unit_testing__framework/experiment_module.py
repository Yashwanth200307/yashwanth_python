'''
Created on 07-Jun-2025

@author: User1
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class OrangeHRMLoginTest_(unittest.TestCase):

    def test_navigation_to_login_page(self):
        '''1. Launching the chrome browser'''
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)

        '''2. Navigate to the login page'''
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        '''3. Validate whether the navigation is successful'''
        expected_url_part = "auth/login"
        actual_url = driver.current_url
        self.assertIn(expected_url_part, actual_url, "Navigation failed")

        '''4. Enter username'''
        username_bx = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username_bx.send_keys("Admin")

        # '''5. Enter password'''
        # password_bx = driver.find_element(By.XPATH, '//*[@type="password"]')
        # password_bx.send_keys("admin123")
        #
        # '''6. Click login button'''
        # login_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
        # login_btn.click()

        '''7. Optional: wait and verify dashboard'''
        time.sleep(2)
        self.assertIn("dashboard", driver.current_url.lower(), "Login might have failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()