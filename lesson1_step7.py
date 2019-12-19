from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x = browser.find_element_by_css_selector('#treasure')
    x = int(x.get_attribute('valuex'))
    browser.find_element_by_css_selector('#answer').send_keys(str(calc(x)))
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Отправляем заполненную форму
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций 28.830720437299842
    browser.quit()
