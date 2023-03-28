from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    browser.maximize_window()
    x_element = browser.find_element(By.CSS_SELECTOR, "span.nowrap#input_value")
    value_x = int(x_element.text)
    y = calc(value_x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()