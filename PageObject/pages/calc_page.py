from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY = (By.ID, "delay")
    PLUS = (By.XPATH, "//span[contains(@class, 'btn-outline-success') and text()='+']")
    MINUS = (By.XPATH, "//span[contains(@class, 'btn-outline-success') and text()='-']")
    DIVIDE = (By.XPATH, "//span[contains(@class, 'btn-outline-success') and text()='÷']")
    MULTIPLY = (By.XPATH, "//span[contains(@class, 'btn-outline-success') and text()='x']")
    EQUALS = (By.XPATH, "//span[contains(@class, 'btn-outline-warning') and text()='=']")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    DOT = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='.']")
    NUMBER_1 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='1']")
    NUMBER_2 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='2']")
    NUMBER_3 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='3']")
    NUMBER_4 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='4']")
    NUMBER_5 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='5']")
    NUMBER_6 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='6']")
    NUMBER_7 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='7']")
    NUMBER_8 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='8']")
    NUMBER_9 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='9']")
    NUMBER_0 = (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='0']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def set_delay(self, seconds):
        input_delay = self.wait.until(EC.presence_of_element_located(self.DELAY))
        input_delay.clear()
        input_delay.send_keys(seconds)

    def click_btn(self, btn):
        element = self.wait.until(EC.element_to_be_clickable(btn))
        element.click()

    def wait_result(self, expected_result):
        self.wait.until(EC.text_to_be_present_in_element(self.SCREEN, expected_result))

    def get_result(self):
        return self.driver.find_element(*self.SCREEN).text
