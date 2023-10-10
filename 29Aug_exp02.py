import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException  # Corrected import

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_exp(driver):
    driver.get("https://www.google.com")

    try:
        element = driver.find_element(By.XPATH, "*//textarea[@id= 'APjFqb']")
        element.click()
    except StaleElementReferenceException as e:
        print("Stale Element Reference Exception:", e.msg)

    driver.refresh()

    try:
        element = driver.find_element(By.XPATH, "*//textarea[@id= 'APjFqb']")
        element.click()
    except StaleElementReferenceException as e:
        print("Stale Element Reference Exception after refresh:", e.msg)
