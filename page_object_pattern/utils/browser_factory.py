from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:
    """
    Factory responsible for creating WebDriver instances.

    Supports browser-specific configuration and execution modes such as headless execution for CI environments.
    """

    @staticmethod
    def get_driver(browser_name="chrome", headless=True):
        browser_name = browser_name.lower()

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
            else:
                options.add_argument("--start-maximized")

            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        if browser_name == "firefox":
            options = webdriver.FirefoxOptions()

            if headless:
                options.add_argument("--headless")
            else:
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")

            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        if browser_name == "edge":
            options = webdriver.EdgeOptions()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
            else:
                options.add_argument("--start-maximized")

            return webdriver.Edge(options=options)

        raise ValueError(f"Unsupported browser: {browser_name}")