import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage
from utilities.base_class import BaseClass
from selenium.webdriver import ActionChains


class TestLogin(BaseClass):

    def test_login_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        # locate the username and password fields and the login button
        login_page = LoginPage(self.driver)
        username_field = login_page.get_username().send_keys("standard_user")
        password_field = login_page.get_password().send_keys("secret_sauce")
        login_button = login_page.get_login_button()

        # click the login button
        login_button.click()

        assert "Swag Labs" in self.driver.title