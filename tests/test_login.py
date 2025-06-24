from pages.login_page import LoginPage

def test_login_success(browser_page):
    login_page = LoginPage(browser_page)
    login_page.goto()
    login_page.login("user", "pass")
    assert browser_page.url == "https://example.com/dashboard" 