import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from shop_page_doc import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title(
    "Оформление заказа: добавление товаров и заполнение данных покупателя"
)
@allure.description(
    "Тест проверяет полный сценарий покупки в интернет-магазине Saucedemo: "
    "авторизация, добавление трёх товаров в корзину, переход в корзину, "
    "оформление заказа с вводом данных и проверку итоговой суммы."
)
@allure.feature("Оформление заказа (Checkout)")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_lesson7(driver):
    with allure.step("Открыть страницу авторизации"):
        login_page = LoginPage(driver).open()

    with allure.step("Выполнить вход под стандартным пользователем"):
        inventory_page = login_page.login_as_standard_user()

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    with allure.step(f"Добавить в корзину товары: {', '.join(products)}"):
        for name in products:
            inventory_page.add_product_by_name(name)

    with allure.step("Перейти в корзину"):
        cart_page = inventory_page.go_to_cart()

    with allure.step("Нажать Checkout в корзине"):
        checkout_page = cart_page.click_checkout()

    with allure.step(
        "Заполнить данные покупателя (имя, фамилия, почтовый индекс)"
    ):
        checkout_page.fill_info(
            first_name="Valera",
            last_name="Tester",
            postal_code="12345"
        )

    with allure.step("Подтвердить ввод данных кнопкой Continue"):
        checkout_page.click_continue()

    with allure.step("Получить итоговую сумму заказа"):
        total_price = checkout_page.get_total_price()

    with allure.step("Проверить, что итоговая сумма равна ожидаемой"):
        assert total_price == "$58.29", (
            f"Ожидалось $58.29, но получено {total_price}"
        )
