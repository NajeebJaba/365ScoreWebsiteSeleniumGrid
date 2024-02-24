from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class SearchTestCase(BasePage):
    SEARCH_ICON = (By.CLASS_NAME, "main-header-module-mobile-buttons-search-icon")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-input")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def perform_search(self, search_query):
        try:
            close_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.close-popup")))
            close_button.click()
        except:
            print("No popup found or not clickable.")

        search_icon = self.wait.until(EC.element_to_be_clickable(self.SEARCH_ICON))
        search_icon.click()

        search_input = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.send_keys(search_query + Keys.RETURN)

    def perform_test(self):
        # navigate to the website and perform a search
        self.navigate_to("https://www.365scores.com/he")
        self.perform_search("search")




