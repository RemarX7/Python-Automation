from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://labirint.ru")

search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)
sleep(5)

#или
#search_buttom = driver.find_element(By.CSS_SELECTOR, ".b-header-b-search-e-srch-icon.b-header-e-sprite-background")
#search_buttom.click()

#Собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

for book in books:
    title = book.find_element(By.CSS_SELECTOR, ".product-card__name").text
    price = book.find_element(By.CSS_SELECTOR, ".product-card__price-current").text
    author = ""

    try:
        author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
    except:
        author = "Автор не указан"

    print(author + "\t" + title + "\t" + price)
    
sleep(5)