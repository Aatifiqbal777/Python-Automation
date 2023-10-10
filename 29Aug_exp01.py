import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  # Import NoSuchElementException

@pytest.fixture
def driver():


def test_exp(driver):
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    try:
        driver.find_element(By.ID, "Aatif")
    except NoSuchElementException as e:
        print("We are not able to find the element:", e. msg)

    driver.get("https://thetestingacademy.com/")

def test_exp_with(driver):
    driver.get("https://app.vwo.com/#/login")

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, "Aatif").click()

    driver.get("https://thetestingacademy.com/")
