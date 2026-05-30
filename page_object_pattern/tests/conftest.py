import os
from datetime import datetime, timedelta

import allure
import pytest
from allure_commons.types import AttachmentType
from page_object_pattern.utils.browser_factory import BrowserFactory


def pytest_addoption(parser):
    """
    Adds custom pytest command-line option for browser selection.

    The selected browser is read from pytest configuration and
    passed to BrowserFactory, which creates the appropriate
    WebDriver instance.
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome"
    )


@pytest.fixture()
def setup(request):
    headless = os.getenv("CI") == "true"

    browser_name = request.config.getoption("--browser")

    driver = BrowserFactory.get_driver(
        browser_name=browser_name,
        headless=headless
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


@pytest.fixture
def flight_date_range():
    today = datetime.now()

    check_in = today + timedelta(days=30)
    check_out = today + timedelta(days=37)

    return {
        "check_in": check_in.strftime("%Y-%m-%d"),
        "check_out": check_out.strftime("%Y-%m-%d")
    }