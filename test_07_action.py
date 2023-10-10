import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.actions.wheel_actions import scrollrigin
from selenium.webdriver import  ActionChains

def test_07_action():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    fromCity = driver.find_element(By.ID, "fromCity")

    actions=ActionChains(driver)
    actions.move_to_element(fromCity).send_keys("New Delhi").perform()

    time.sleep(5)