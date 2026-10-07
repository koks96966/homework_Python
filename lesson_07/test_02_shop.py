import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from shop_pages import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_lesson7(driver):
    login_page = LoginPage(driver).open()
    inventory_page = login_page.login_as_standard_user()
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    for name in products:
        inventory_page.add_product_by_name(name)

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.click_checkout()

    checkout_page.fill_info(
        first_name="Valera",
        last_name="Tester",
        postal_code="12345"
    )
    checkout_page.click_continue()
    total_price = checkout_page.get_total_price()
    assert total_price == "$58.29", (
        f"Ожидалось $58.29, но получено {total_price}"
    )
