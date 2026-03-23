from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    driver = webdriver.Edge()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        fields_and_locators = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'job-position': "QA",
            'company': "SkyPro"
        }

        for key, value in fields_and_locators.items():
            input_field = driver.find_element(By.NAME, key)
            input_field.send_keys(value)

        driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )

        zip_code = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code.get_attribute("class")

        for locator in fields_and_locators:
            if locator != 'zip-code':
                element = driver.find_element(By.ID, locator)
                assert "alert-success" in element.get_attribute("class")

    finally:
        driver.quit()
