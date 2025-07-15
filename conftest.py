import os
import pytest
import pathlib
from data.urls import Urls
from playwright.sync_api import Page, expect
from data.users import get_user_creds_by_role

STORAGE_DIR = "storage"


BROWSER_CONTEXT_OPTS = {
    "viewport": {"width": 1920, "height": 1080},
}

def login(page: Page, role: str):
    email, password = get_user_creds_by_role(role)
    page.goto(Urls.LOGIN_PAGE)
    page.fill("//input[@id='login_email']", email)
    page.fill("//input[@id='password']", password)
    page.click("//input[@id='gdpr_checkbox']")
    page.click("//button[@id='loginformsubmit']")
    expect(page.locator("//h4[contains(@class, 'welcome-title')]")).to_be_visible(timeout=10000)

def _context_page_for_role(role: str, browser):
    state_file = os.path.join(STORAGE_DIR, f"{role}.json")
    if os.path.exists(state_file):
        context = browser.new_context(
            storage_state=str(state_file),
            **BROWSER_CONTEXT_OPTS
        )
        return context, context.new_page()
    context = browser.new_context(**BROWSER_CONTEXT_OPTS)
    page = context.new_page()
    login(page, role)
    context.storage_state(path=str(state_file))
    return context, page

@pytest.fixture
def page(browser):
    context, page = _context_page_for_role("admin", browser)
    yield page
    page.close()
    context.close()

@pytest.fixture
def manager(browser):
    context, page = _context_page_for_role("manager", browser)
    yield page
    page.close()
    context.close()