from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
from login_page import LoginPage

EMAIL = "example@gmail.com"
PASSWORD = "password"

driver = webdriver.Chrome()
driver.maximize_window()

try:
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(2)

    login_page.enter_username(EMAIL)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    time.sleep(5)
    driver.save_screenshot("invalid_login_attempt.png")
    print(" Screenshot saved: invalid_login_attempt.png")

    try:
        # Detect login failure
        driver.find_element(By.XPATH, '//div[contains(text(), "invalid") or contains(text(), "refresh")]')
        print(" Invalid login detected. Trying Google login...")

        login_page.click_continue_with_google()
        time.sleep(4)

        driver.save_screenshot("after_google_click.png")
        print("Screenshot saved: after_google_click.png")

    except NoSuchElementException:
        print("No error message found — login may have succeeded or CAPTCHA blocked detection.")

except Exception as e:
    print("Error during test:", e)

finally:
    driver.quit()
