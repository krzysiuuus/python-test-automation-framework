import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta



@pytest.fixture()
def setup(request):
    #driver = DriverFactory.get_driver("chrome")
    options = webdriver.ChromeOptions()
    #options.add_argument("--ignore-certificate-errors")
    #options.add_argument("--allow-insecure-localhost")
    options.binary_location = r"C:\Users\kstyczynski\PycharmProjects\chrome-win64\chrome.exe"
    service = Service(executable_path=r"C:\Users\kstyczynski\PycharmProjects\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    #driver.quit()

@pytest.fixture
def date_range():
    today = datetime.today()
    check_in = today + timedelta(days=7)
    check_out = today + timedelta(days=8)

    return {
        "check_in": check_in.strftime("%d/%m/%Y"),
        "check_out": check_out.strftime("%d/%m/%Y")
    }