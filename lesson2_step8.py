from selenium import webdriver
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)
    browser.find_element_by_css_selector('[name="firstname"]').send_keys('Дмитрий')
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('Куликов')
    browser.find_element_by_css_selector('[name="email"]').send_keys('noname@noname.com')
    file = browser.find_element_by_id('file')
    file.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Отправляем заполненную форму
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций 28.87758942985154
    browser.quit()
