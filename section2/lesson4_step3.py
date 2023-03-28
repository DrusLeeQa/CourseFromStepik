import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(3)

try:
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.maximize_window()
    button = browser.find_element(By.CSS_SELECTOR, "button#verify")
    button.click()
    message = browser.find_element(By.CSS_SELECTOR, "div#verify_message")
    assert "successful!" in message.text

finally:
    time.sleep(5)
    browser.quit()
