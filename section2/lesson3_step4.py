from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.maximize_window()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = float(x_element.text)
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()