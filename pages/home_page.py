from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomeLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_user_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(HomeLocators.USER_DROPDOWN)).click()

    def click_logout(self):
        self.wait.until(
            EC.visibility_of_element_located(HomeLocators.DROPDOWN_MENU)
        )
        self.wait.until(EC.element_to_be_clickable(HomeLocators.LOGOUT_LINK)).click()

    def logout(self):
        self.click_user_dropdown()
        self.click_logout()