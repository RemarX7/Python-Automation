from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    google = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
    google.send_keys("Selenium", Keys.RETURN)
    sleep(5)
    checkbox = driver.find_element(By.CSS_SELECTOR, "recaptcha-checkbox-border").click()
    sleep(5)

finally:    
    driver.quit()
