from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.checkout_page import CheckoutPage


class CartPage:

    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_checkout(self):
        checkout = (By.ID, "checkout")
        self.wait.until(EC.element_to_be_clickable(checkout)).click()
        return CheckoutPage(self.driver)

    def get_cart_items_names(self):
        items = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
            )
        return [item.text for item in items]

    def is_current_page_cart(self):
        return self.driver.current_url == self.URL
