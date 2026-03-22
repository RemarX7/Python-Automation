from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()

    try:
        driver.implicitly_wait(5)
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        backpack = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        checkout = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "checkout"))
        ).click()
        driver.find_element(By.ID, "first-name").send_keys("Alexander")
        driver.find_element(By.ID, "last-name").send_keys("Kerlanov")
        driver.find_element(By.ID, "postal-code").send_keys("999999")
        driver.find_element(By.ID, "continue").click()

        total_price = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label"))
        )

        assert total_price.text == "Total: $58.29"

    finally:
        driver.quit()
