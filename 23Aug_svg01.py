#svg mpa

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_js_executed(driver):
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)

    path_states = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in path_states:
        state_name = state.get_attribute("aria-label")
        print(state_name)

        if state_name == "Tripura ":
            actions.move_to_element(state).click().perform()
            break
    time.sleep(5)

