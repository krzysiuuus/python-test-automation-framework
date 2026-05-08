import allure
import pytest
import os
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    if os.getenv("CI"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()

@pytest.fixture
def date_range():
    today = datetime.today()
    check_in = today + timedelta(days=7)
    check_out = today + timedelta(days=8)

    return {
        "check_in": check_in.strftime("%d/%m/%Y"),
        "check_out": check_out.strftime("%d/%m/%Y")
    }