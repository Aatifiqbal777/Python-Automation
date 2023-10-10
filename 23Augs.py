#svg

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_js_executed(driver):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("AC")
    time.sleep(5)

    search_svg_icon= driver.find_element(By.XPATH,"//*[local-name()='svg']/*[local-name()='g' and@faill-rule='evenodd']")
    search_svg_icon= driver.find_element(By.XPATH,"//button[@type='submit']//*[name()='svg']")
    action = ActionChains(driver)
    action.move_to_element(search_svg_icon).click().perform()
    time.slee(3)
