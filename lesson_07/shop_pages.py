from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class LoginPage:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CLASS_NAME, "btn_action")

    def open(self, base_url="https://www.saucedemo.com"):
        self.driver.get(base_url)
        return self

    def login_as_standard_user(self):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        )
        password_field = self.driver.find_element(*self.password_input)
        login_btn = self.driver.find_element(*self.login_button)

        username_field.clear()
        username_field.send_keys("standard_user")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        login_btn.click()
        return InventoryPage(self.driver, self.wait)


class InventoryPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_container a")

    def add_product_by_name(self, product_name: str):
        xpath_expr = (
            "//div[contains(@class, 'inventory_item') "
            f"and .//*[contains(text(), '{product_name}')]]"
        )
        card = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath_expr))
        )
        add_button = card.find_element(By.CSS_SELECTOR, ".btn_primary")
        add_button.click()
        return self

    def go_to_cart(self):
        link = self.wait.until(EC.element_to_be_clickable(self.cart_link))
        link.click()
        return CartPage(self.driver, self.wait)


class CartPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.checkout_btn = (By.CSS_SELECTOR, ".checkout_button")
        self.cart_title = (By.CLASS_NAME, "shopping_cart_container")

    def click_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.checkout_btn))
        btn.click()
        return CheckoutPage(self.driver, self.wait)


class CheckoutPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_btn = (By.CSS_SELECTOR, ".cart_button")
        self.total_price = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_info(self, first_name, last_name, postal_code):
        fname_field = self.wait.until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        fname_field.clear()
        fname_field.send_keys(first_name)

        lname_field = self.driver.find_element(*self.last_name_input)
        lname_field.clear()
        lname_field.send_keys(last_name)

        postal_field = self.driver.find_element(*self.postal_code_input)
        postal_field.clear()
        postal_field.send_keys(postal_code)
        return self

    def click_continue(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.continue_btn)
        )
        btn.click()
        return self

    def get_total_price(self):
        el = self.wait.until(
            EC.visibility_of_element_located(self.total_price)
        )
        text = el.text
        match = re.search(r"\$\d+\.\d{2}", text)
        if not match:
            raise ValueError("Не удалось извлечь сумму из текста: " + text)
        return match.group()
