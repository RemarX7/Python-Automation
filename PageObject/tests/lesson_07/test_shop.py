from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    assert login_page.is_current_page_login()

    login_page.input_username('standard_user')
    login_page.input_password('secret_sauce')
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_current_page_inventory()

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Bolt T-Shirt')
    inventory_page.add_to_cart('Sauce Labs Onesie')
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_current_page_cart()

    cart_items = cart_page.get_cart_items_names()
    assert set(cart_items) == {"Sauce Labs Backpack",
                               "Sauce Labs Bolt T-Shirt",
                               "Sauce Labs Onesie"}
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    assert checkout_page.is_current_page_chekout()

    checkout_page.input_first_and_last_names('Itachi', 'Utiha')
    checkout_page.input_postal_code('888888')
    checkout_page.click_continue()
    assert checkout_page.is_current_page_total()
    assert checkout_page.get_total_price() == '$58.29'
    print(f"Итоговая сумма: {checkout_page.get_total_price()}")
