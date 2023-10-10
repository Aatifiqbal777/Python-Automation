import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.actions.wheel_actions import scrollrigin
from selenium.webdriver import  ActionChains

def test_06_action():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    #iframe = driver.find_element(By.TAG_NAME, "iframe")

    #ActionChains(driver).scroll_to_element(iframe).perform()

    #time.sleep(50)