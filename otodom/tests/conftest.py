import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page_object_pattern.utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    #driver = DriverFactory.get_driver("chrome")
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\kstyczynski\PycharmProjects\chrome-win64\chrome.exe"
    service = Service(executable_path=r"C:\Users\kstyczynski\PycharmProjects\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service)
    #driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    #driver.quit()