from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)
    browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(0.5)
    browser.switch_to_window(browser.window_handles[-1])
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()  # Отправляем заполненную форму
    time.sleep(1)
    alert = browser.switch_to_alert()
    text = alert.text
    text = text.split(':')[1]
    print(text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #input('Ну?')
    # закрываем браузер после всех манипуляций 28.878496474581677
    browser.quit()
