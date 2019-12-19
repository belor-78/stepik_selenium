from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox()
    browser.get(link)
    WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    browser.find_element_by_id('book').click()
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    button = browser.find_element_by_css_selector("#solve")
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
