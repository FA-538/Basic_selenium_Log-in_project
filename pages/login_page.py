from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(LoginLocators.USERNAME_INPUT)).send_keys(username)

    def error_username(self):
        self.wait.untill(
            EC.visibility_of_element_located(LoginLocators.ERROR_USERNAME_INPUT))

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)

    def eerror_password(self):
        self.driver.find_element(*LoginLocators.ERROR_PASSWORD_INPUT)

    def click_login(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_invalid_credentials_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(LoginLocators.INVALID_CREDENTIALS_MESSAGE)
        ).text

    def get_required_field_errors(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(LoginLocators.REQUIRED_FIELD_ERRORS)
        )

    def is_login_button_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON)
        ).is_displayed()