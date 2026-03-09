from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("https://ya.ru")


sleep(10)
