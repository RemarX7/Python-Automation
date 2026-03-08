from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    btn_sky = driver.find_element(
        By.CSS_SELECTOR, ".btn.btn-primary")
    btn_sky.click()
    sleep(5)

finally:
    driver.quit()
