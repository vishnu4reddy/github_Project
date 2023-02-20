from playwright.sync_api import expect


class test_LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('//*[@id="login_field"]]')
        self.password = page.locator('//*[@id="password"]')
        self.login_button = page.locator("input[value='Sign in']")
        # self.home_button = page.locator("button[id=react-burger-menu-btn]")

    def navigate(self):
        self.page.goto("https://github.com/login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        expect(self.home_button).to_be_visible()