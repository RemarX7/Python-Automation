from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_txt = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_txt.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

btn = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro") 
)
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()
