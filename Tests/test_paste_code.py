from Page_Object.login_page_po import LoginPage
from playwright.sync_api import Page
from Data import config
Email = config.user_git
password = config.git_pass
number = config.number


def test_check_login(page: Page):

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(Email, password)
    login_page.repositories()
    login_page.test_files()
    login_page.Codespaces()
    login_page.Codespace()

    LoginPage(page)
