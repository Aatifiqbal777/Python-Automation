import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_js_executed(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    js_ex = driver.execute_script
    element = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    js_ex("arguments[0].click()", element)

    title = js_ex("return document.title")
    print(title)
    btn_add = driver.find_element(By.CLASS_NAME,"added-manually")
    print(btn_add)
    time.sleep(3)

    driver.get("https://thetestingacademy.com/")
    js_ex("window.scrollBy(0,1000)")
    time.sleep(2)

