from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_on_Edge():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 20)

    try:
        start_url = (
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        driver.get(start_url)
        driver.maximize_window()
        wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

        # Заполняем форму
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "job-position": "QA",
            "company": "SkyPro",
        }
        for name_val, value in fields.items():
            el = wait.until(
                EC.visibility_of_element_located((By.NAME, name_val))
            )
            el.clear()
            if value:
                el.send_keys(value)

        submit_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        submit_btn.click()

        # Шаг 1: ждём, пока URL изменится
        wait.until(EC.url_changes(start_url))

        # Шаг 2: ждём появления алерта с ошибкой для zip-code (alert-danger)
        error_alert = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        assert "N/A" in error_alert.text, (
            f"В алерт-ошибке нет текста 'N/A'. Текст: {error_alert.text}"
        )

        # Шаг 3: ждём появления алерта успеха (alert-success)
        success_alert = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".alert-success")
            )
        )
    finally:
        driver.quit()
