from playwright.sync_api import Page, sync_playwright
import time
from Data import config
Email = config.user_git
password = config.git_pass
number = config.number


def test_github(page: Page):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     context = browser.new_context(
    #         record_video_dir="./record_videos/",
    #         record_video_size={"width": 640, "height": 480}
    #     )
    #     page = context.new_page()
    print("Starting On Earth")
    time.sleep(3)
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("github")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshot1.png", full_page=True)
    page.locator("//a[normalize-space()='+.Git Hub Login']").click()
    page.locator("//input[@id='login_field']").click()
    page.locator("//input[@id='login_field']").fill(Email)
    page.keyboard.press("Tab")
    page.keyboard.type(password)
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    page.close()

# from playwright.sync_api import expect


# class test_LoginPage:
# def __init__(self, page):
#     self.page = page
#     self.username = page.locator('//*[@id="login_field"]]')
#     self.password = page.locator('//*[@id="password"]')
#     self.login_button = page.locator("input[value='Sign in']")
#     # self.home_button = page.locator("button[id=react-burger-menu-btn]")

# def navigate(self):
#     self.page.goto("https://github.com/login")

# def login(self, username, password):
#     self.username.fill(username)
#     self.password.fill(password)
#     self.login_button.click()
#     expect(self.home_button).to_be_visible()



