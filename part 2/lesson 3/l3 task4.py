from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    # Работает с int
    return str(math.log(abs(12 * math.sin(x))))


def solve_quize(browser):
    """Содержит calc"""

    # Читаем значение x и вычисляем ответ
    x = int(browser.find_element(By.ID, "input_value").text)
    answer = calc(x)

    # Вводим ответ
    browser.find_element(By.TAG_NAME, "input").send_keys(answer)

def main():
    try:
        # Открываем страницу
        link = "http://suninjuly.github.io/alert_accept.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Жмем кнопку
        browser.find_element(By.TAG_NAME, "button").click()

        # Соглашаемся с окном предупреждения
        alert = browser.switch_to.alert
        alert.accept()

        # Решаем задачу
        solve_quize(browser)
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").submit()

    finally:
        # Копируем ответ
        time.sleep(30)

        # Закрываем браузер
        browser.quit()


if __name__ == "__main__":
    main()