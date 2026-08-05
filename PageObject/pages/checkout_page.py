from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    URL_CHECKOUT = "https://www.saucedemo.com/checkout-step-one.html"
    URL_TOTAL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def input_first_and_last_names(self, first, last):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))
                        ).send_keys(first)
        self.wait.until(EC.presence_of_element_located((By.ID, "last-name"))
                        ).send_keys(last)

    def input_postal_code(self, code):
        self.wait.until(EC.presence_of_element_located((By.ID, "postal-code"))
                        ).send_keys(code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))
                        ).click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text.replace("Total: ", "")
        return total_text

    def is_current_page_chekout(self):
        return self.driver.current_url == self.URL_CHECKOUT

    def is_current_page_total(self):
        return self.driver.current_url == self.URL_TOTAL
