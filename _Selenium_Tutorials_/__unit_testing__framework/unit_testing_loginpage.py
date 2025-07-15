'''
Created on 07-Jun-2025

@author: User1
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class OrangeHRMLoginTest(unittest.TestCase):

    def setUp(self):
        # 1. Launching the Chrome browser
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_valid_login_navigation_and_dashboard(self):
        driver = self.driver

        # 2. Navigate to login page
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        # 3. Validate current URL contains "auth/login"
        expected_login_url = "auth/login"
        actual_url = driver.current_url
        self.assertIn(expected_login_url, actual_url, "Login page navigation failed!")

        # 4. Enter username
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys("Admin")

        # 5. Enter password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("admin123")

        # 6. Click Login
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        # 7. Wait for redirection (basic wait; for better use WebDriverWait)
        time.sleep(3)

        # 8. Validate successful login by checking URL or element on Dashboard
        expected_dashboard_url = "dashboard/index"
        actual_url = driver.current_url
        self.assertIn(expected_dashboard_url, actual_url, "Dashboard navigation failed after login!")

    def test_invalid_login_should_fail(self):
        driver = self.driver

        # Navigate to login page
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        # Enter invalid credentials
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys("InvalidUser")
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("InvalidPass")

        # Click Login
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        # Wait for error message to appear
        time.sleep(2)
        
        # Validate error is displayed
        error_message = driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
        self.assertTrue(error_message.is_displayed(), "Error message not shown for invalid login!")

if __name__ == "__main__":
    unittest.main()
