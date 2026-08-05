from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage


class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_cart(self, product_name):
        formatted_name = product_name.lower().replace(' ', '-')
        locator = (By.ID, f"add-to-cart-{formatted_name}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def go_to_cart(self):
        cart_prod = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.wait.until(EC.element_to_be_clickable(cart_prod)).click()
        return CartPage(self.driver)

    def is_current_page_inventory(self):
        return self.driver.current_url == self.URL
