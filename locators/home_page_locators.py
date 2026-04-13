from selenium.webdriver.common.by import By


class HomeLocators:
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    DROPDOWN_MENU = (By.CSS_SELECTOR, "ul.oxd-dropdown-menu[role='menu']")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")