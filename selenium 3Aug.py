import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwologin():
    LOGGER = logging.getLogger(__name__)

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://app.vwo.com")

 email_address_ele = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_address_ele = driver.find_element(By.XPATH, "//input[@name='username']")
    email_address_ele = driver.find_element(By.XPATH, "//input[@data-qa='hocewoqisi']")

    password_ele = driver.find_element(By.NAME, "password")

    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    email_address_ele.send_keys("93npu2yyb0@esiix.com")
    password_ele.send_keys("Wingify@123")

    sign_in_button_ele.click()

    time.sleep(5)

    LOGGER.info('title is ->  ' + driver.title)


    assert "Dashboard" intime.driver.title