from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class FavoritesTestCase(BasePage):
    FAVORITES_ICON = (By.CSS_SELECTOR, "img.star-icon-spin-close.clickable")

    def perform_test(self):
        self.driver.get("https://www.365scores.com/he")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FAVORITES_ICON))
        favorites_icon = self.driver.find_element(*self.FAVORITES_ICON)
        assert favorites_icon.is_displayed(), "Favorites icon is not displayed."



"run it"
# from selenium.webdriver.common.by import By
# from infra.base_page import BasePage
#
# class FavoritesTestCase(BasePage):
#     # Updated CSS selector to match the provided class names
#     FAVORITES_ICON = (By.CSS_SELECTOR, "img.star-icon-spin-close.clickable")
#
#     def verify_favorites_section_displayed(self):
#         favorites_icon = self.driver.find_element(*self.FAVORITES_ICON)
#         return favorites_icon.is_displayed()
#
#     def perform_test(self):
#         # Navigate to the website and verify the favorites section is displayed
#         self.navigate_to("https://www.365scores.com/hefavori")  # Adjust URL as necessary
#         assert self.verify_favorites_section_displayed(), "Favorites icon is not displayed."
#
#         from selenium.webdriver.common.by import By
#         from selenium.webdriver.support.ui import WebDriverWait
#         from selenium.webdriver.support import expected_conditions as EC
#         from infra.base_page import BasePage
#
#         class FavoritesTestCase(BasePage):
#             FAVORITES_ICON = (By.CSS_SELECTOR, "img.star-icon-spin-close.clickable")
#
#             def perform_test(self):
#                 self.driver.get("https://www.365scores.com/he")
#                 WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FAVORITES_ICON))
#                 favorites_icon = self.driver.find_element(*self.FAVORITES_ICON)
#                 assert favorites_icon.is_displayed(), "Favorites icon is not displayed."
