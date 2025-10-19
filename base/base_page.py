from playwright.sync_api import Page
import os

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def take_screenshot(self, name: str):
        os.makedirs("test_results/screenshots", exist_ok=True)
        self.page.screenshot(path=f"test_results/screenshots/{name}.png")