import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from utilities.base_class import BaseClass
from selenium.webdriver.support.ui import WebDriverWait

    
class TestGoogle(BaseClass):
    
    def test_google_page_elements(self):
    # Open the Google page
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(5)

    # Assert the page title
        expected_title = "Google"
        assert expected_title in self.driver.title, f"Expected title: {expected_title}, but got: {driver.title}"

    # Assert the presence of the superior menu (Google apps menu)
        superior_menu_locator = (By.CLASS_NAME,"gb_0d")
        assert self.driver.find_element(By.CLASS_NAME,"gb_0d").is_displayed(), "Superior menu is not displayed"

    # Assert the presence of the search bar
        search_bar_locator = (By.NAME, "q")
        assert self.driver.find_element(By.NAME, "q").is_displayed(), "Search bar is not displayed"

