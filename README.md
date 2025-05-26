**Selenium Automation Test – Replit Login and Google Redirect**

This project automates the login process on Replit.com using Selenium WebDriver and the Page Object Model in Python.
The script attempts to log in using intentionally on both valid and invalid credentials. If the login fails, it detects the error and automatically clicks the "Continue with Google" button. This approach demonstrates form interaction, error detection, conditional flows, and element handling with XPath and JavaScript execution.

**Features**

Organized using the Page Object Pattern
Automates form fill and button clicks on the Replit login page
Uses XPath selectors for precision
Login if valid credentials
Detects login error messages
Clicks the "Continue with Google" button upon failed login
Captures screenshots at key points during the test


**Technologies Used**

Python 3
Selenium WebDriver
ChromeDriver
XPath selectors
JavaScript execution in Selenium

**Folder Structure**

project_folder/

├── login_page.py - Page Object class

├── test_replit_login.py - Main test script

├── valid_login_attempt.png - Screenshot after login attempt

├──invalid_login_attempt.png - Screenshot after login attempt

**How to Run**

Install Selenium:
pip install selenium
Download ChromeDriver:
https://chromedriver.chromium.org/downloads
Ensure the version matches your installed Chrome browser.

**Run the script:**

python test_replit_login.py

**Notes**

The test uses intentionally incorrect credentials to simulate login failure, in case of login failure, it will show "invalid credentials" take screenshoot and redirect towards Continue with google.
Incase of valid credentials, it shows "Your captcha token is invalid. Please refresh the page and try again", and takes screenshoot.
Screenshots are saved locally to verify the flow and outcomes.

**Screenshots**

valid_login_attempt.png: Captured after submitting valid login credentials
invalid_login_attempt.png: Captured after submitting invalid login credentials

**Author**

Husnain Ali
Eötvös Loránd University (ELTE), Hungary
