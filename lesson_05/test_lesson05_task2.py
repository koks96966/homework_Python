from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online/forms/post")

    wait = WebDriverWait(driver, 10)
    name_input = wait.until(
        EC.presence_of_element_located((By.NAME, "custname"))
        )
    name_input.send_keys("Валерий")

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Submit order']")
    ))
    submit_button.click()

    assert driver.current_url != "https://httpbin.qa-territory.online/post"

    driver.quit()
