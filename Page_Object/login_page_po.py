# from playwright.sync_api import sync_playwright,Page


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('//*[@id="login_field"]')
        self.password = page.locator('//*[@id="password"]')
        self.login_button = page.locator("//input[@name='commit']")
        self.seemore = page.locator(
            "(//button[@name='button'][normalize-space()='Show more'])[1]")
        self.perticular_repositories = page.locator(
            "//img[@alt='Post_Rolex_Linkedin_sel']")
        self.test_folder = page.get_by_role("link", name="Tests")
        self.test_file = page.locator(
            "//a[normalize-space()='test_share_post.py']")
        self.copy_file = page.locator(
            "//remote-clipboard-copy[@class='d-inline-block btn-octicon']")
        self.codespaces = page.get_by_role("link", name="Codespaces")
        self.configuration = page.get_by_role(
            "button", name="Codespace configuration")
        self.browser = page.locator(
            "//button[@data-action='click:options-popover#showEditors']")
        self.select_browser = page.locator(
            "//span[normalize-space()='Open in browser']")
        self.codespace = page.locator(
            "//span[contains(text(),'Tests')]")
        self.codespace_file = page.locator(
            "//span[contains(text(),'test_sample.py')]")
        self.wholespace = page.locator(
            "//div[@class='view-lines monaco-mouse-cursor-text']")
        self.control_1 = page.keyboard
        self.control_2 = page.keyboard
        self.control_3 = page.keyboard
        self.terminal = page.locator("//canvas[@class='xterm-cursor-layer']")
        self.t_control_1 = page.keyboard
        self.t_control_2 = page.keyboard
        self.t_control_3 = page.keyboard
        self.t_control_4 = page.keyboard
        # self.t_control_1 = page

    def navigate(self):
        self.page.goto("https://github.com/login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def repositories(self):
        self.seemore.click()
        self.perticular_repositories.click()

    def test_files(self):
        self.test_folder.click()
        self.test_file.click()
        self.copy_file.click()

    def Codespaces(self):
        self.codespaces.click()
        self.configuration.click()
        self.browser.click()
        self.select_browser.click()

    def Codespace(self):
        self.codespace.click()
        self.codespace_file.click()
        self.wholespace.click()
        self.control_1.press("Control+A")
        self.control_2.press("Backspace")
        self.control_3.press("Control+V")

    def Terminal(self):
        self.terminal.click()
        self.t_control_1.type("clear", delay=10)
        self.t_control_2.press("Enter")
        self.t_control_3.type("pytest test _sample.py", delay=10)
        self.t_control_4.press("Enter")
