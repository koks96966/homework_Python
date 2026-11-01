import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page_doc import CalculatorPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Тест проверяет корректность работы калькулятора на странице "
    "slow-calculator"
    "при установленной задержке 45 секунд: ввод 7 + 8, ожидание результата 15."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_lesson7(driver):
    page = CalculatorPage(driver, timeout=50)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    with allure.step("Открыть страницу калькулятора"):
        driver.get(url)

    with allure.step("Установить задержку вычислений на 45 секунд"):
        page.set_delay(45)

    try:
        with allure.step("Ввести последовательность 7 + 8 ="):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Дождаться появления результата '15' на экране"):
            page.wait_result("15")

        with allure.step("Получить текст результата и проверить его"):
            actual_result = page.get_result_text()
            assert actual_result == "15", (
                f"Ожидался результат 15, но получили {actual_result}"
            )
    except Exception as e:
        # Сохраняем скриншот при ошибке — он автоматически подхватится Allure
        driver.save_screenshot("error_screenshot.png")
        allure.attach.file(
            "error_screenshot.png",
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG,
        )
        raise e
