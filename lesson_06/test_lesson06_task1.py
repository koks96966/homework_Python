from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    # 2. Найдите и нажмите на кнопку "Start"
    start_button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[normalize-space()='Start']"
        ))
    )
    start_button.click()
    # 3. Дождитесь появления текста "Hello World!"
    hello_text_element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    # 4. Сделайте скриншот страницы
    driver.save_screenshot("lesson_06/dynamic_loading_hello_world.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert hello_text_element.text == "Hello World!", (
        f"Ожидался 'Hello World!', но получен: '{hello_text_element.text}'"
    )
    driver.quit()
