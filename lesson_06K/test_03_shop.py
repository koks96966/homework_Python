import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)

    wait = WebDriverWait(driver, 20)

    # Авторизация
    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CLASS_NAME, "btn_action")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    # Добавляем в корзину товары
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "inventory_list")
    ))

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    for product_name in products_to_add:
        xpath_expr = (
            "//div[contains(@class, 'inventory_item') "
            f"and .//*[text()='{product_name}']]"
        )

        product_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath_expr)
            )
        )
        add_button = product_card.find_element(By.CSS_SELECTOR, ".btn_primary")
        add_button.click()

    cart_link = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_container a")
    ))
    cart_link.click()

    checkout_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout_button"))
    )
    checkout_button.click()
    # Заполняем форму своими данными
    first_name_input = wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Valera")
    last_name_input.send_keys("Pankov")
    postal_code_input.send_keys("12345")

    continue_button = driver.find_element(By.CSS_SELECTOR, ".cart_button")
    continue_button.click()

    # Ждём именно URL чекаута
    wait.until(lambda d: d.current_url.endswith("/checkout-step-two.html"))

    # Дополнительная диагностика: выводим URL и title, если дальше будет ошибка
    print(f"Current URL: {driver.current_url}")
    print(f"Page title: {driver.title}")

    # Ищем элемент с итоговой суммой
    total_element = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".summary_total_label")
    ))
    total_text = total_element.text.strip()
    print(f"Total text found: '{total_text}'")

    # Парсим: текст вида "Total: $58.29"
    total_value = total_text.replace("Total: ", "").strip()
    assert total_value == "$58.29", (
        f"Ожидалось $58.29, но получено: {total_value}"
    )
