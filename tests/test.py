"""run it"""
import unittest
import concurrent.futures
from infra.config_handler import ConfigHandler
from infra.browser_wrapper import BrowserWrapper
from logic.search_test_case import SearchTestCase
from logic.live_score_test_case import LiveScoreTestCase
from logic.favorites_test_case import FavoritesTestCase
from logic.contact_us_test_case import ContactUsTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GridTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.HUB_URL = cls.config["hub_url"]
        cls.browsers = cls.config["browser_types"]

    def close_popup_if_present(self, driver):
        try:

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.close, button.accept"))).click()
            print("Popup closed or accepted.")
        except Exception as e:
            # if no popup is found or clickable, print a message and continue
            print(f"No popup found or not clickable: {e}")

    def run_test_on_browser(self, browser_name):
        browser_wrapper = BrowserWrapper(browser_name)
        driver = browser_wrapper.initialize_driver()
        try:
            driver.get(self.config["url"])  # navigate to the site
            self.close_popup_if_present(driver)  # close any popup if present

            search_test = SearchTestCase(driver)
            search_test.perform_test()

            live_score_test = LiveScoreTestCase(driver)
            live_score_test.perform_test()

            favorites_test = FavoritesTestCase(driver)
            favorites_test.perform_test()

            contact_us_test = ContactUsTestCase(driver)
            contact_us_test.perform_test()

        finally:
            driver.quit()

    def test_website_on_multiple_browsers(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers)) as executor:
            futures = {executor.submit(self.run_test_on_browser, browser): browser for browser in self.browsers}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"{browser} test encountered an exception: {e}")


if __name__ == "__main__":
    unittest.main()














"""running on the first two test cases :search , live_score (but the test cases in one test) """
# import time
# import unittest
# from selenium import webdriver
# from infra.browser_wrapper import BrowserWrapper
# from logic.search_test_case import SearchTestCase
# from logic.live_score_test_case import LiveScoreTestCase
# from infra.config_handler import ConfigHandler
# import concurrent.futures
#
#
# class GridTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.config_handler = ConfigHandler()
#         cls.config = cls.config_handler.config
#         cls.HUB_URL = cls.config["hub_url"]
#         cls.browsers = cls.config["browser_types"]
#
#     def run_test_on_browser(self, browser_name):
#         browser_wrapper = BrowserWrapper(browser_name)
#         driver = browser_wrapper.initialize_driver()
#         try:
#             # Assuming the URL is set in your BrowserWrapper or here
#             driver.get("https://www.365scores.com")  # Make sure this is set correctly
#
#             # Running search test case
#             search_test = SearchTestCase(driver)
#             search_test.perform_search("Football")
#             # Here, you would validate the search was successful
#
#             # Running live score test case
#             live_score_test = LiveScoreTestCase(driver)
#             self.assertTrue(live_score_test.verify_live_score_displayed(),
#                             f"Live score section not displayed in {browser_name}")
#         finally:
#             driver.quit()
#         time.sleep(5)
#
#     def test_website_on_multiple_browsers(self):
#         with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browsers)) as executor:
#             # Launch tests in parallel
#             futures = {executor.submit(self.run_test_on_browser, browser): browser for browser in self.browsers}
#             for future in concurrent.futures.as_completed(futures):
#                 browser = futures[future]
#                 try:
#                     future.result()
#                 except Exception as e:
#                     print(f"{browser} test encountered an exception: {e}")
#
#
# if __name__ == "__main__":
#     unittest.main()


















