from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    cookies_user_1 = {
        "name": "SESSION",
        "value": "MzBlYzlkOTctMGIwYy00ZDZkLTkzNjQtYmM3MjZlYzc4ZWFk",
        "domain": "gitflic.ru",
        "path": "/",
    }
    cookies_user_2 = {
        "name": "SESSION",
        "value": "ZGFmZTU2N2YtMDIwNy00MjI3LWFlOTItYWZiNWU3NTNlMzEx",
        "domain": "gitflic.ru",
        "path": "/",
    }

    profile_url_user_1 = "https://gitflic.ru/user/koks96966"
    profile_url_user_2 = "https://gitflic.ru/user/ygol"

    try:
        # Шаг 1. Открываем страницу
        driver.get("https://gitflic.ru/")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Шаг 2. Устанавливаем cookie пользователя 1
        driver.add_cookie(cookies_user_1)
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Шаг 3. Переходим на страницу пользователя 1
        driver.get(profile_url_user_1)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        url_user_1 = driver.current_url
        print("URL пользователя 1:", url_user_1)

        # Шаг 4. Разлогиниваемся
        driver.delete_all_cookies()

        # Шаг 5. Снова открываем страницу и ставим cookie пользователя 2
        driver.get("https://gitflic.ru/")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        driver.add_cookie(cookies_user_2)
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Шаг 6. Переходим на страницу пользователя 2
        driver.get(profile_url_user_2)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        url_user_2 = driver.current_url
        print("URL пользователя 2:", url_user_2)

        # Шаг 7. Проверка
        assert url_user_1 != url_user_2, (
            f"URL совпадают: {url_user_1} == {url_user_2}"
        )
        print("Тест пройдён: URL различаются.")

    finally:
        driver.quit()
