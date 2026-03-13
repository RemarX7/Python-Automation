from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.maximize_window()

my_cookie = {
    "name": "cookie policy",
    "value": "1"
}
driver.get("https://labirint.ru/")
driver.add_cookie(my_cookie)

cookies = driver.get_cookies()
print(cookies)

#driver.delete_all_cookies()
#driver.refresh()

#sleep(10)
driver.quit()