from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_INPUT = (By.NAME, "username")
    #ERROR_USERNAME_INPUT = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span")
    PASSWORD_INPUT = (By.NAME, "password")
    PASSWORD_INPUT = (By.NAME, "password")
    #ERROR_PASSWORD_INPUT = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    INVALID_CREDENTIALS_MESSAGE = (
        By.XPATH,
        "//p[contains(@class,'oxd-alert-content-text')]"
    )
    REQUIRED_FIELD_ERRORS = (
        By.XPATH,
        "//span[normalize-space()='Required']"
    )