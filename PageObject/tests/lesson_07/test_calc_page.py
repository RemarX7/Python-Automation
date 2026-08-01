from pages.calc_page import CalcPage


def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calc_page = CalcPage(driver)
    calc_page.set_delay(45)
    calc_page.click_btn(CalcPage.NUMBER_7)
    calc_page.click_btn(CalcPage.PLUS)
    calc_page.click_btn(CalcPage.NUMBER_8)
    calc_page.click_btn(CalcPage.EQUALS)

    calc_page.wait_result("15")
    result = calc_page.get_result()
    assert result == "15"
