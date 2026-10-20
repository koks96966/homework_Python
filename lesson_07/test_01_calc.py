import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_lesson7(driver):
    page = CalculatorPage(driver, timeout=50)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    page.set_delay(45)

    try:
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")
    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        raise e

    page.wait_result("15")
    actual_result = page.get_result_text()
    assert actual_result == "15", (
        f"Ожидался результат 15, но получили {actual_result}"
    )
