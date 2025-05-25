from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = '//input[@name="username"]'
        self.password_field = '//input[@name="password"]'
        self.login_button = '//button[@data-cy="log-in-btn"]'
        self.google_button_xpath = "//button[div[text()='Continue with Google']]"

    def load(self):
        self.driver.get("https://replit.com/login")

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_continue_with_google(self):
        print(" Trying to click 'Continue with Google' button...")

        try:
            google_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.google_button_xpath))
            )

            # Highlight the button
            self.driver.execute_script("arguments[0].style.border='3px solid red'", google_btn)
            # Delay to help you visually confirm highlight
            WebDriverWait(self.driver, 2).until(lambda d: True)

            # Click using JavaScript
            self.driver.execute_script("arguments[0].click();", google_btn)
            print(" Clicked 'Continue with Google' button.")

        except Exception as e:
            print(" Failed to click Google button:", e)
