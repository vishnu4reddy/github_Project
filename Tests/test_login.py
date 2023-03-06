from Page_Object.login_page_po import LoginPage
from playwright.sync_api import 
from Data import config
Email = config.user_git
password = config.git_pass


def test_check_login(page4):

    login_page = LoginPage(page4)
    login_page.navigate()
    login_page.login(Email, password)
