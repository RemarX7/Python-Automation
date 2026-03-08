from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input = driver.find_element(By.CSS_SELECTOR, "input")
    input.send_keys("12345")
    sleep(1)
    input.clear()
    input.send_keys("54321")
    sleep(2)

finally:
    driver.quit()
