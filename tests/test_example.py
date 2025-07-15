import time
import allure
import pytest
from base.base_test import BaseTest


class TestAuthDemo(BaseTest):

    @pytest.mark.all
    @allure.title("Example of automatic test")
    def test_example(self):
        self.login_page().open()
