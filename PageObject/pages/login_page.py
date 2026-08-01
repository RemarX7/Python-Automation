from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def input_username(self, username):
        input_name = self.wait.until(
            EC.presence_of_element_located(self.USERNAME))
        input_name.clear()
        input_name.send_keys(username)

    def input_password(self, password):
        input_pass = self.wait.until(
           EC.presence_of_element_located(self.PASSWORD))
        input_pass.clear()
        input_pass.send_keys(password)

    def click_login(self):
        self.wait.until(
              EC.element_to_be_clickable((By.ID, "login-button"))).click()
        return InventoryPage(self.driver)

    def is_current_page_login(self):
        return self.driver.current_url == self.URL
