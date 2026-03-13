from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

selectors = ["#compass", "#calendar", "#award", "#landscape"]

for selector in selectors:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )

print(driver.find_element(By.CSS_SELECTOR, selectors[2]).get_attribute("src"))

driver.quit()
