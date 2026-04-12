from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_user_dropdown(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))).click()

    def click_logout(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.oxd-dropdown-menu[role='menu']"))
        )
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

    def logout(self):
        self.click_user_dropdown()
        self.click_logout()