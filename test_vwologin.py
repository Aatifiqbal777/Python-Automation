import time

import allure
import pytest
from load_env import load_env


@allure.epic("VWO App Positive")
@allure.feature("Login Positive Test")
class TestVWoLogin:
    @pytest.mark.usefixtures("setup")
    def test_vwologin(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(3)