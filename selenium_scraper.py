from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://twitter.com/GTNUK1"
driver.get(url)

try:
    # Wait for the email input form to become visible
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "r-30o5oe"))
    )
    email_input.send_keys(email)

    # Wait for the next button to become clickable
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[role="button" and @type="button" and contains(., "Next")]'))
    )
    next_button.click()

    # Wait for the password input form to become visible
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(password)

    current_screen = driver.current_window_handle
    window_handles = driver.window_handles
    for handle in window_handles:
        if handle != current_screen:
            driver.switch_to.window(handle)
            break

    # Add assertion to verify the new window title
    assert "Expected Title" in driver.title, "Title does not match"

except Exception as e:
    print(f"An error occurred: {e}")