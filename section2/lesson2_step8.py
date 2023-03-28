from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.maximize_window()
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Bob")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Marley")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("Bob_Marley@gmail.com")
    file = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    file.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()