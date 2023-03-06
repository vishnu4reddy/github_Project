import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def page4(pytestconfig):
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(headless=True)
        print(pytestconfig.getoption("--headed"))
        # print(pytestconfig)
        # context = browser.new_context()
        page = browser.new_page()
        yield page
