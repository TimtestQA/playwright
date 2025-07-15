import allure
from playwright.sync_api import Page

class BasePage:

    _PAGE_URL: str = ""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open page")
    def open(self):
        self.page.goto(self._PAGE_URL)
        self.page.wait_for_load_state("networkidle")