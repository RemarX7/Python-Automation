from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_calculator():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(45)

        seven = driver.find_element(
            By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='7']").click()

        plus = driver.find_element(
            By.XPATH, "//span[contains(@class, 'btn-outline-success') and text()='+']").click()

        eight = driver.find_element(
            By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='8']").click()

        start_time = time.time()

        equally = driver.find_element(
            By.XPATH, "//span[contains(@class, 'btn-outline-warning') and text()='=']").click()

        WebDriverWait(driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )

        end_time = time.time()
        elapsed_time = end_time - start_time

        assert 44.5 <= elapsed_time <= 45.5

    finally:
        driver.quit()
