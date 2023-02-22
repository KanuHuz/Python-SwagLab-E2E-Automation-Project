from selenium.webdriver.common.by import By
from selenium import webdriver


class CheckOutPageOne:

    def __init__(self, driver):
        self.driver = driver

    hamburger_button = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")
    continue_shopping_button = (By.CSS_SELECTOR, "#continue")
    cancel_button = (By.CSS_SELECTOR, "#cancel")
    firstname = (By.CSS_SELECTOR, "#first-name")
    lastname = (By.CSS_SELECTOR, "#last-name")
    postal_code = (By.CSS_SELECTOR, "#postal-code")
    checkout_page_title = (By.CSS_SELECTOR, ".title")
    app_logo = (By.CSS_SELECTOR, ".app_logo")

    def get_hamburger_button(self):
        return self.driver.find_element(*CheckOutPageOne.hamburger_button)

    def get_cart_button(self):
        return self.driver.find_element(*CheckOutPageOne.cart_button)

    def get_continue_shopping_button(self):
        return self.driver.find_element(*CheckOutPageOne.continue_shopping_button)

    def get_cancel_button(self):
        return self.driver.find_element(*CheckOutPageOne.cancel_button)

    def get_firstname(self):
        return self.driver.find_element(*CheckOutPageOne.firstname)

    def get_lastname(self):
        return self.driver.find_element(*CheckOutPageOne.lastname)

    def get_postal_code(self):
        return self.driver.find_element(*CheckOutPageOne.postal_code)

    def get_checkout_page_title(self):
        return self.driver.find_element(*CheckOutPageOne.checkout_page_title)

    def get_app_logo(self):
        return self.driver.find_element(*CheckOutPageOne.app_logo)

