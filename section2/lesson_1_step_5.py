import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    #Считывание значения x и вычисление выражения
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    #Ввод ответа в текстовое поле
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)
    
    #Установка чек-бокса
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    
    #Уставнока переключателя
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    
    #Нажатие кнопки
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
    time.sleep(10)

finally:
    browser.quit()
