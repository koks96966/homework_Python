from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.qa-territory.online/links/10")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

        links = driver.find_elements(By.TAG_NAME, "a")

        assert len(links) == 9, f"Ожидалось 9 ссылок, найдено: {len(links)}"

        for i, link in enumerate(links):
            assert link.is_displayed()

        first_link_text = links[0].text.strip()
        assert "1" in first_link_text, f"Текст первой ссылки содержит '1': '{first_link_text}'"

    finally:
        driver.quit()
