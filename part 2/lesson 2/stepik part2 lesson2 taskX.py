from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

# Открываем страницу
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Заполняем поля
browser.find_element(By.CSS_SELECTOR, "input[name=firstname]").send_keys("Максик")
browser.find_element(By.CSS_SELECTOR, "input[name=lastname]").send_keys("Mercury")
browser.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("y@yandex.ru")

# Ищем файл на пк
current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'bio.txt') # добавляем к этому пути имя файла

# Выбираем файл на сайте
browser.find_element(By.ID, "file").send_keys(file_path)

# Отправляем все
browser.find_element(By.CSS_SELECTOR, "button[type=submit]").submit()

# Копируем ответ
time.sleep(3)

# Закрываем браузер
browser.quit()


# element.send_keys(file_path)

# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Читаем значение x и вычисляем ответ
#     x = int(browser.find_element(By.ID, "input_value").text)
#     answer = calc(x)
#
#     # Листаем вниз
#     browser.execute_script("window.scrollBy(0, 100);")
#
#     # Вводим ответ
#     browser.find_element(By.TAG_NAME, "input").send_keys(answer)
#
#     # Листаем до кнопки button
#     button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
#     button.location_once_scrolled_into_view
#
#     # Прожимаем боксы
#     browser.find_element(By.ID, "robotCheckbox").click()
#     browser.find_element(By.ID, "robotsRule").click()
#
#     # Отправляем ответ
#     button.click()
#     time.sleep(3)
#
#
# finally:
#     time.sleep(3)
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
# from selenium.webdriver.support.ui import Select
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Читаем значение x и вычисляем ответ
#     x = int(browser.find_element(By.ID, "input_value").text)
#     answer = calc(x)
#
#     # Листаем вниз
#     browser.execute_script("window.scrollBy(0, 100);")
#
#     #Вводим ответ
#     browser.find_element(By.TAG_NAME, "input").send_keys(answer)
#
#     # Прожимаем боксы
#     browser.find_element(By.ID, "robotCheckbox").click()
#     browser.find_element(By.ID, "robotsRule").click()
#
#     # Отправляем ответ
#
#     browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
#     time.sleep(3)
#
#
# finally:
#     time.sleep(3)
#     browser.quit()
# __________________________________
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# __________________________________________________
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()
# ______________________________________________
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.get("https://SunInJuly.github.io/execute_script.html")
#
# try:
#     time.sleep(3)
#     button = driver.find_element(By.TAG_NAME, "button")
#     button.location_once_scrolled_into_view
#     button.click()
#     time.sleep(3)
#
# finally:
#     driver.quit()
# ___________________

