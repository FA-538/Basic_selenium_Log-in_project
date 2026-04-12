from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.login("Admin", "admin123")
    home_page.logout()