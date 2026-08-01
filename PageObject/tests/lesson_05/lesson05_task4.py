from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    input_username = driver.find_element(By.CSS_SELECTOR, "#username")
    input_username.send_keys("tomsmith")
    sleep(1)

    input_password = driver.find_element(By.CSS_SELECTOR, "#password")
    input_password.send_keys("SuperSecretPassword!")
    sleep(1)

    button = driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    sleep(1)

finally:
    driver.quit()
