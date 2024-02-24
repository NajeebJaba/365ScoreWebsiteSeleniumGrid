from selenium.webdriver.common.by import By
from infra.base_page import BasePage

class LiveScoreTestCase(BasePage):
    LIVE_SCORE_SECTION = (By.CSS_SELECTOR, "div.switch-button-content")

    def verify_live_score_displayed(self):
        live_score = self.driver.find_element(*self.LIVE_SCORE_SECTION)
        return live_score.is_displayed()

    def perform_test(self):
        # navigate to the website and verify the live score display
        self.navigate_to("https://www.365scores.com/he")  # Adjust URL as necessary
        assert self.verify_live_score_displayed(), "Live score section not displayed."









