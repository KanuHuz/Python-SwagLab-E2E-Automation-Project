from selenium.webdriver.common.by import By
from selenium import webdriver


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    hamburger_button = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    exit_menu_button = (By.CSS_SELECTOR, "#react-burger-cross-btn")
    all_items_option = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    about_option = (By.CSS_SELECTOR, "#about_sidebar_link")
    logout_option = (By.CSS_SELECTOR, "#logout_sidebar_link")
    reset_app_state_option = (By.CSS_SELECTOR, "#reset_sidebar_link")
    cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")
    sorting_button = (By.CSS_SELECTOR, ".product_sort_container")
    swag_logo = (By.CSS_SELECTOR, ".app_logo")
    twitter_logo = (By.CSS_SELECTOR, "a[href='https://twitter.com/saucelabs']")
    facebook_logo = (By.CSS_SELECTOR, "a[href='https://www.facebook.com/saucelabs']")
    linkedin_logo = (By.CSS_SELECTOR, "a[href='https://www.linkedin.com/company/sauce-labs/']")
    inventory_list = (By.CSS_SELECTOR, ".inventory_list")  # we have to iterate through this to find the add/remove buttons
    remove_item_button = (By.CSS_SELECTOR, ".btn_secondary.btn_inventory")
    add_item_button = (By.CSS_SELECTOR, ".btn_primary.btn_inventory")

    def get_hamburger_button(self):
        return self.driver.find_element(*InventoryPage.hamburger_button)

    def get_exit_menu_button(self):
        return self.driver.find_element(*InventoryPage.exit_menu_button)

    def get_all_items_option(self):
        return self.driver.find_element(*InventoryPage.all_items_option)

    def get_about_option(self):
        return self.driver.find_element(*InventoryPage.about_option)

    def get_logout_option(self):
        return self.driver.find_element(*InventoryPage.logout_option)

    def get_reset_app_state_option(self):
        return self.driver.find_element(*InventoryPage.reset_app_state_option)

    def get_cart_button(self):
        return self.driver.find_element(*InventoryPage.cart_button)

    def get_sorting_button(self):
        return self.driver.find_element(*InventoryPage.sorting_button)

    def get_swag_logo(self):
        return self.driver.find_element(*InventoryPage.swag_logo)

    def get_twitter_logo(self):
        return self.driver.find_element(*InventoryPage.twitter_logo)

    def get_facebook_logo(self):
        return self.driver.find_element(*InventoryPage.facebook_logo)

    def get_linkedin_logo(self):
        return self.driver.find_element(*InventoryPage.linkedin_logo)

    def get_inventory_list(self):
        return self.driver.find_element(*InventoryPage.inventory_list)

    def get_remove_item_button(self):
        return self.driver.find_element(*InventoryPage.remove_item_button)

    def get_add_item_button(self):
        return self.driver.find_element(*InventoryPage.add_item_button)
