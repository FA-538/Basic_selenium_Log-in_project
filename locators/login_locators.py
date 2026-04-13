from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    INVALID_CREDENTIALS_MESSAGE= (
        By .XPATH,"//p[contains(@class, 'oxd-alert-content-text')]"

    )

    REQUIRED_FIELD_ERROR =  (
        By.XPATH,
        "//span[contains(@class,'oxd-input-field-error-message')]"
    )

