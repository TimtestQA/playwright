import pytest
from pages.login_page import LoginPage

class BaseTest:

    @pytest.fixture(autouse=True)
    def _setup(self, request, page):
        self.login_page = lambda p=page: LoginPage(p)
