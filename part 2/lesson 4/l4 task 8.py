from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait


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
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ищем кнопку Book
        button = browser.find_element(By.ID, "book")

        # Ждем пока цена станет 100$
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

        # Жмем кнопку Book
        button.click()

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



