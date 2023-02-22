from selenium.webdriver.common.by import By
from selenium import webdriver


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    continue_shopping_button = (By.CSS_SELECTOR, "#continue-shopping")
    checkout_button = (By.CSS_SELECTOR, "#checkout")
    cart_list = (By.CSS_SELECTOR, ".cart_list")  # we have to iterate through this to find the add/remove buttons
    cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")
    hamburger_button = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    exit_menu_button = (By.CSS_SELECTOR, "#react-burger-cross-btn")
    all_items_option = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    about_option = (By.CSS_SELECTOR, "#about_sidebar_link")
    logout_option = (By.CSS_SELECTOR, "#logout_sidebar_link")
    reset_app_state_option = (By.CSS_SELECTOR, "#reset_sidebar_link")
    swag_logo = (By.CSS_SELECTOR, ".app_logo")
    twitter_logo = (By.CSS_SELECTOR, "a[href='https://twitter.com/saucelabs']")
    facebook_logo = (By.CSS_SELECTOR, "a[href='https://www.facebook.com/saucelabs']")
    linkedin_logo = (By.CSS_SELECTOR, "a[href='https://www.linkedin.com/company/sauce-labs/']")
    cart_page_title = (By.CSS_SELECTOR, ".title")

    def get_hamburger_button(self):
        return self.driver.find_element(*CartPage.hamburger_button)

    def get_exit_menu_button(self):
        return self.driver.find_element(*CartPage.exit_menu_button)

    def get_all_items_option(self):
        return self.driver.find_element(*CartPage.all_items_option)

    def get_about_option(self):
        return self.driver.find_element(*CartPage.about_option)

    def get_logout_option(self):
        return self.driver.find_element(*CartPage.logout_option)

    def get_reset_app_state_option(self):
        return self.driver.find_element(*CartPage.reset_app_state_option)

    def get_cart_button(self):
        return self.driver.find_element(*CartPage.cart_button)

    def get_swag_logo(self):
        return self.driver.find_element(*CartPage.swag_logo)

    def get_twitter_logo(self):
        return self.driver.find_element(*CartPage.twitter_logo)

    def get_facebook_logo(self):
        return self.driver.find_element(*CartPage.facebook_logo)

    def get_linkedin_logo(self):
        return self.driver.find_element(*CartPage.linkedin_logo)

    def get_cart_page_title(self):
        return self.driver.find_element(*CartPage.cart_page_title)

    def checkout_button(self):
        return self.driver.find_element(*CartPage.checkout_button)

