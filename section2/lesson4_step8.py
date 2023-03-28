from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    browser.maximize_window()
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
    book = browser.find_element(By.CSS_SELECTOR, 'button#book')
    book.click()
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = float(x_element.text)
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
