import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelectors(unittest.TestCase):
    def test_page1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        css_selectors = ['.first_block input.first',
                         '.first_block input.second',
                         '.first_block input.third']
        for css in css_selectors:
            essential_line = browser.find_element(By.CSS_SELECTOR, css)
            essential_line.send_keys("a@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироватьсяя
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Вы не смогли зарегистрироваться.")

    def test_page2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        css_selectors = ['.first_block input.first',
                         '.first_block input.second',
                         '.first_block input.third']
        for css in css_selectors:
            essential_line = browser.find_element(By.CSS_SELECTOR, css)
            essential_line.send_keys("a@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироватьсяя
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Вы не смогли зарегистрироваться")
