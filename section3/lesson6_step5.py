import time
import math
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('link', links)
def test_authorization(browser, link):
    url = link
    browser.get(url)
    browser.maximize_window()
    login_1 = WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login")))
    login_1.click()
    email = WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
    email.send_keys("milenak214@gmail.com")
    password = WebDriverWait(browser, 8).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    password.send_keys("Drusisback14!02")
    login_2 = WebDriverWait(browser, 8).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_2.click()
    avatar = WebDriverWait(browser, 8).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='User avatar'].navbar__profile-img")))
    answer = math.log(int(time.time()))
    input_field = WebDriverWait(browser, 8).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area.textarea")))
    input_field.send_keys(answer)
    send = WebDriverWait(browser, 8).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    send.click()
    feedback = WebDriverWait(browser, 8).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span.attempt-message_correct")))
    optional_feedback = WebDriverWait(browser, 8).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))
    assert optional_feedback.text == "Correct!", f"expected 'Correct!', got '{optional_feedback.text}'"
