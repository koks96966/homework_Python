from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver, timeout=120):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_screen = (By.CLASS_NAME, "screen")
        self._calculator_container = (By.ID, "calculator")

    def set_delay(self, seconds: int):
        element = self.wait.until(
            EC.visibility_of_element_located(self._delay_input)
        )
        element.clear()
        element.send_keys(str(seconds))
        return self

    def click_button(self, label: str):
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

    def wait_result(self, expected_text: str):
        self.wait.until(EC.text_to_be_present_in_element(
            self._result_screen, expected_text
        ))
        return self

    def get_result_text(self) -> str:
        result_el = self.wait.until(
            EC.visibility_of_element_located(self._result_screen)
        )
        return result_el.text.strip()
