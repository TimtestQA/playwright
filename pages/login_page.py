# pages/contacts_page.py
from data.urls import Urls
from playwright.sync_api import Page
from base.base_page import BasePage


class LoginPage(BasePage):

    _PAGE_URL = Urls.LOGIN_PAGE

    def click(self):
        ...


