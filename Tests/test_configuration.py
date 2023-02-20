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
    page.screenshot(path="screenshot2.png", full_page=True)
    page.get_by_role("link", name="Sign in").click()
    page.locator(
        "//form[@action='/dashboard/ajax_my_repositories?location=left']//button[@name='button'][normalize-space()='Show more']").click()
    page.locator(
        "//ul[2]//li[2]//div[1]//div[1]//a[1]").click()
    page.get_by_role("link", name="Tests").click()
    page.get_by_role("link", name="test_Share.py").click()
    page.locator(
        "//remote-clipboard-copy[@class='d-inline-block btn-octicon']").click()
    page.screenshot(path="screenshot3.png", full_page=True)
    page.get_by_role("link", name="Codespaces").click()
    page.get_by_role("button", name="Codespace configuration").click()
    page.close()