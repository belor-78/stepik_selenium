from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)
    x = int(browser.find_element_by_css_selector("#input_value").text)
    field = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);",field)
    field.send_keys(calc(x))
    robot_check_box = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           robot_check_box)
    robot_check_box.click()
    robot_check_box = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           robot_check_box)
    robot_check_box.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Отправляем заполненную форму
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций 28.87758942985154
    browser.quit()
