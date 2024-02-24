from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from infra.config_handler import ConfigHandler

class BrowserWrapper:
    def __init__(self, browser_name="chrome"):
        self.config_handler = ConfigHandler()
        self.config = self.config_handler.config
        self.browser_name = browser_name
        self.driver = None

    def initialize_driver(self):
        if self.browser_name.lower() == "chrome":
            options = ChromeOptions()
            # Add logging options for Chrome
            options.add_argument("--enable-logging")
            options.add_argument("--v=1")  # Adjust log level as needed
        elif self.browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
        elif self.browser_name.lower() == "edge":
            options = EdgeOptions()

        else:
            raise ValueError("Unsupported browser")

        if self.config["grid"]:
            self.driver = webdriver.Remote(
                command_executor=self.config["hub_url"],
                options=options
            )
        else:
            if self.browser_name.lower() == "chrome":
                self.driver = webdriver.Chrome(options=options)
            elif self.browser_name.lower() == "firefox":
                self.driver = webdriver.Firefox(options=options)
            elif self.browser_name.lower() == "edge":
                self.driver = webdriver.Edge(options=options)

        self.driver.get(self.config["url"])
        return self.driver