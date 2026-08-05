from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    btn_sky = driver.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    btn_sky.click()
    sleep(2)

    alert = driver.switch_to.alert
    print(f"Текст алерта: {alert.text}")
    alert.accept()
    sleep(2)

finally:
    driver.quit()
