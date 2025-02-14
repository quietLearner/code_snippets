import os
import time
from pathlib import Path

from dotenv import load_dotenv

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

degugging = True
USER_NAME = os.getenv("tan_id")
PASSWORD = os.getenv("tan_password")
URL = os.getenv("url")
print(USER_NAME, PASSWORD)

script_location = Path(__file__).resolve().parent
driver_path = script_location / "chromedriver-win64" / "chromedriver.exe"
print(driver_path.exists())


chrome_options = Options()
if degugging:
    # keep chome open
    chrome_options.add_experimental_option("detach", True)
else:
    # do not open browser
    chrome_options.add_argument("--headless")


def wait_for_element(driver, by, selector, timeout=10):
    try:
        element_present = EC.presence_of_all_elements_located((by, selector))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Time out wating for {selector}")
        return None

    return driver.find_element(By.ID, selector)


def login(driver):
    driver.get(URL)

    username_input = wait_for_element(driver, By.ID, "username")
    submit_btn = wait_for_element(driver, By.ID, "LogInBtn")

    if username_input and submit_btn:
        username_input.send_keys(USER_NAME)
        submit_btn.click()


def security_question_page(driver):
    driver.get("https://www.ezcardinfo.com/login/security-question")


def main():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        login(driver)
    except WebDriverException as e:
        print(f"{e}")
    finally:
        if not degugging:
            driver.quit()


if __name__ == "__main__":
    main()
