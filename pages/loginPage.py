from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")
    bot_image = (By.CSS_SELECTOR, "#.bot_column")
    login_logo = (By.CSS_SELECTOR, ".login_logo")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_bot_image(self):
        return self.driver.find_element(*LoginPage.bot_image)

    def get_login_logo(self):
        return self.driver.find_element(*LoginPage.login_logo)

