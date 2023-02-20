from Page_Object.login_page_po import test_LoginPage
from playwright.sync_api import Page
# import time
from Data import config
Email = config.user_git
password = config.git_pass
number = config.number


def test_check_login(page: Page):

    login_page = test_LoginPage(page)
    login_page.navigate()

    test_LoginPage(page)
