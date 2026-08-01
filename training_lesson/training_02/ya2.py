from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def make_screenshoot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru")
    sleep(5)

    browser.save_screenshot('./ya_'+browser.name+'.png')
    browser.quit()

chrome = webdriver.Chrome()
edge = webdriver.Edge()
firefox = webdriver.Firefox()

make_screenshoot(chrome)
make_screenshoot(edge)
make_screenshoot(firefox)