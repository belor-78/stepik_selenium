from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Firefox()
    browser.get(link)
    first = int(browser.find_element_by_css_selector("#num1").text)
    second = int(browser.find_element_by_css_selector("#num2").text)
    ans = str(first + second)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(ans)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Отправляем заполненную форму
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций 28.876227168910482
    # 28.87622720696267
    browser.quit()
