# test windows by actions
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_07_action():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    main_window_handle = driver.current_window_handle
    print(main_window_handle)
    link = driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()

    window_handle = driver.window_handles
    print(window_handle)

    for handle in window_handle:
       driver.switch_to.window(handle)
       if "New Window"in driver.page_source:
           print("Found the Text")
           break

    driver.switch_to.window(main_window_handle)
    time.sleep(10)