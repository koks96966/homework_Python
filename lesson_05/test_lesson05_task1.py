from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    form_link.click()

    assert driver.current_url.endswith("/forms/post")

    driver.back()

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()
