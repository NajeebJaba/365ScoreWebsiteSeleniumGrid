"""run it"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class ContactUsTestCase(BasePage):
    CONTACT_US_LINK = (By.CSS_SELECTOR, "a.footer_link__95Kv0")  # Updated CSS selector

    def verify_contact_us_accessible(self):
        contact_us_link = self.driver.find_element(*self.CONTACT_US_LINK)
        contact_us_link.click()
        # Wait until the page title contains "Contact Us"
        return self.wait_until_title_contains("Contact Us")

    def wait_until_title_contains(self, text, timeout=10):
        """Wait until the page title contains a specific text."""
        return WebDriverWait(self.driver, timeout).until(EC.title_contains(text))

    def perform_test(self):
        # Navigate to the website and verify the contact us page is accessible
        self.navigate_to("https://www.365scores.com/he")  # Adjust URL as necessary
        assert self.verify_contact_us_accessible(), "Contact Us page is not accessible."








