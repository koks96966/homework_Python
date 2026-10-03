import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_delay_45(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    wait = WebDriverWait(driver, 50)

    # 1. Вводим задержку 45 в поле #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 2. Нажимаем кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 3. Ждём результат «15»
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15"
    ))

    actual_result = driver.find_element(By.CLASS_NAME, "screen").text
    assert actual_result == "15", (
        f"Ожидался результат 15, но получили {actual_result}"
    )
