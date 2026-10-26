from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница калькулятора (slow-calculator)."""

    def __init__(self, driver, timeout: int = 120) -> None:
        """
        :param driver: selenium.webdriver — экземпляр драйвера браузера.
        :param timeout: int — таймаут ожидания элементов в секундах.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_screen = (By.CLASS_NAME, "screen")
        self._calculator_container = (By.ID, "calculator")

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Устанавливает задержку вычислений калькулятора.
        :param seconds: int — количество секунд задержки.
        :return: CalculatorPage — возвращает себя для цепочки вызовов.
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self._delay_input)
        )
        element.clear()
        element.send_keys(str(seconds))
        return self

    def click_button(self, label: str) -> "CalculatorPage":
        """
        Нажимает кнопку калькулятора по текстовой метке.
        :param label: str — текст кнопки (например, '7', '+', '=').
        :return: CalculatorPage — возвращает себя для цепочки вызовов.
        """
        # Сначала убедимся, что контейнер калькулятора присутствует
        self.wait.until(
            EC.presence_of_element_located(self._calculator_container)
        )

        xpath_template = (
            "//div[@id='calculator']//span["
            "contains(normalize-space(), '{}')]"
        )
        locator = (By.XPATH, xpath_template.format(label))

        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()
        return self

    def wait_result(self, expected_text: str) -> "CalculatorPage":
        """
        Ожидает появления ожидаемого текста в поле результата.
        :param expected_text: str — ожидаемый текст результата.
        :return: CalculatorPage — возвращает себя для цепочки вызовов.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self._result_screen, expected_text
            )
        )
        return self

    def get_result_text(self) -> str:
        """
        Получает текущий текст из поля результата.
        :return: str — текст результата без лишних пробелов.
        """
        result_el = self.wait.until(
            EC.visibility_of_element_located(self._result_screen)
        )
        return result_el.text.strip()
