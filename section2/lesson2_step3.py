from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
    browser.maximize_window()
    first_number = browser.find_element(By.CSS_SELECTOR, "#num1")
    value_first_number = int(first_number.text)
    second_number = browser.find_element(By.CSS_SELECTOR, "#num2")
    value_second_number = int(second_number.text)
    total = str(value_first_number + value_second_number)
    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_value(total)
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
