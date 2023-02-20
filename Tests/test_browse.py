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