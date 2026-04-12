from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_valid_login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.oxd-dropdown-menu[role='menu']")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()
