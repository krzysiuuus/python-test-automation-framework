from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BrowserFactory:

    @staticmethod
    def get_driver(browser_name="chrome", headless=True):
        if browser_name.lower() == "chrome":
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

        raise ValueError(f"Unsupported browser: {browser_name}")