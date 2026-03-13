from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ya.ru")

#element = driver.find_element(By.CSS_SELECTOR, "#text")
#element.send_keys("test")
#element.click()
#print(element)

txt = driver.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').text
tag = driver.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').tag_name
id = driver.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').id
href = driver.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').get_attribute("href")
ff = driver.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').value_of_css_property("font-family")
color = driver.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').value_of_css_property("color")

print(txt)
print(tag)
print(id)
print(href)
print(ff)
print(color)

sleep(10)
driver.quit()
