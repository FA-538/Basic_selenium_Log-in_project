from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class login_page():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def get_username(self,username):
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).clear()
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    def get_password(self,password):
        self.find_element(By.NAME, "password")
        self.find_element(By.NAME,"password").send_keys("password")
    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def login(self, username, password):
        self.get_username(username)
        self.get_password(password)
        self.click_login()

