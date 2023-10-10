import time

import allure
import pytest
from allure_commons.types import AttachmentType



@allure.epic("vwo App")
@allure.feature("Login test")
class TestVWoLogin:


    @pytest.mark.usefixtures("setup")
    def test_vwoLogin_negative(self, setup):
        driver = setup
        driver.get(self.base_url)  # Define self.base_url or pass it as an argument
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd="123")
        time.sleep(5)

        if "Dashboard2" in driver.title:
            # Capture and attach a screenshot
            allure.attach(driver.get_screenshot_as_png(), name="testLoginscreen", attachment_type=AttachmentType.PNG)

        assert "Dashboard" in driver.title
        time.sleep(3)

    @pytest.mark.usefixtures("setup")

    def test_vwoLogin_pf(self, setup):
        driver = setup
        driver.get(self.base_url)  # Define self.base_url or pass it as an argument
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)  # Define self.password or pass it as an argument
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(3)
