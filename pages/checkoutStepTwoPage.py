from selenium.webdriver.common.by import By
from selenium import webdriver


class CheckOutPageTwo:

    def __init__(self, driver):
        self.driver = driver

    checkout_overview_title = (By.CSS_SELECTOR, ".title")
    cancel_button = (By.CSS_SELECTOR, "#cancel")
    finish_button = (By.CSS_SELECTOR, "#finish")
    item_total = (By.CSS_SELECTOR, ".summary_subtotal_label")
    item_tax = (By.CSS_SELECTOR, ".summary_tax_label")
    total_sum = (By.CSS_SELECTOR, ".summary_total_label")

    def get_checkout_overview_title(self):
        return self.driver.find_element(*CheckOutPageTwo.checkout_overview_title)

    def get_cancel_button(self):
        return self.driver.find_element(*CheckOutPageTwo.cancel_button)

    def get_finish_button(self):
        return self.driver.find_element(*CheckOutPageTwo.finish_button)

    def get_item_total(self):
        return self.driver.find_element(*CheckOutPageTwo.item_total)

    def get_item_tax(self):
        return self.driver.find_element(*CheckOutPageTwo.item_tax)

    def get_total_sum(self):
        return self.driver.find_element(*CheckOutPageTwo.total_sum)