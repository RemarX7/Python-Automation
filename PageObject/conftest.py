import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "profile.password_manager_leak_detection": False,
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
