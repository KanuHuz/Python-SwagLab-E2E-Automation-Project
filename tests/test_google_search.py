import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from utilities.base_class import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
import time

    
class TestGoogle(BaseClass):

    def test_google_search(self):

    # Open the Google page
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(3)
    
    # Assert the presence of the search box
        search_box = self.driver.find_element(By.NAME, "q")
        assert self.driver.find_element(By.NAME, "q").is_displayed(), "Search box is not displayed"
        search_text = "teting"
        search_box.send_keys("teting")
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        
    # Assert that we are on the search results page and suggestion gets displayed
        print(self.driver.current_url)
        assert "google.com/search" in self.driver.current_url, "Not on search results page."
        assert self.driver.find_element(By.CLASS_NAME, "gL9Hy d2IKib").is_displayed(), "Suggestion not displayed as expected"
        did_you_mean_prompt = self.driver.find_element(By.CLASS_NAME, "gL9Hy d2IKib")
        suggested_term = self.driver.find_element(By.CLASS_NAME, "gL9Hy")
        suggested_term.click()
        time.sleep(3)
    
    # Validate appropriate results get displayed using suggested term
        assert "testing" in self.driver.current_url, "The term 'testing' is not present in the URL."
        search_box_value = self.driver.find_element(By.NAME, "q").get_attribute("value")
        assert "testing" in search_box_value, "The term 'testing' is not present in the search box."
        search_results_array = self.driver.find_elements_by_css_selector(".yuRUbf")
        first_search_result = search_results_array[0]   
        search_title = first_search_result.find_element_by_css_selector(".DKV0Md").text
        assert "testing" in search_title, f"Word 'Testing' not found in the first search result: '{search_title}'"

    # Click on images tab
        images_tab = self.driver.find_element(By.CLASS_NAME, "GKS7s")
        images_tab.click()
        assert self.driver.find_element(By.CLASS_NAME, "IwRct"), "The image carousel is not present"


        