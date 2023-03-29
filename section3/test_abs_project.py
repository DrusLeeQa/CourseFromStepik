import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    def open_browser(self, link):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get(link)
        self.browser.maximize_window()

    def test_reg1(self):
        self.open_browser(self.link1)
        self.input1 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        self.input1.send_keys("Bob")
        self.input2 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        self.input2.send_keys("Marley")
        self.input3 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        self.input3.send_keys("bob_marley@gmail.com")
        self.button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text,
                         "Welcome text not equal Congratulations! You have successfully registered!")
        self.browser.quit()

    def test_reg2(self):
        self.open_browser(self.link2)
        self.input1 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        self.input1.send_keys("Bob")
        self.input2 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        self.input2.send_keys("Marley")
        self.input3 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        self.input3.send_keys("bob_marley@gmail.com")
        self.button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text,
                         "Welcome text not equal Congratulations! You have successfully registered!")
        self.browser.quit()
