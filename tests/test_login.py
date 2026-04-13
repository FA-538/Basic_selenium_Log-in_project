from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.login("Admin", "admin123")
    home_page.logout()

def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.login("Admin", "wrong123")

    error_message = login_page.get_invalid_credentials_message()
    assert "Invalid credentials" in error_message


def test_empty_credentials(driver):
    login_page = LoginPage(driver)

    login_page.click_login()

    errors = login_page.get_required_field_errors()
    assert len(errors) == 2