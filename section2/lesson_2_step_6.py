import math
import time
from selenium import webdriver

def f_str(x):
    return str(math.log(abs(12*math.sin(float(x))), math.e))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)
    
    #Поиск значения x и вычисление значения функции
    x = browser.find_element_by_id("input_value").text
    y = f_str(x)
    
    #Скролл с помощью кнопки
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
    
    #Ввод ответа в текстовое поле
    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)
    
    #Чекбокс
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    #Переключатель
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    #Кнопка
    button.click()
    
    time.sleep(10)

finally:
    browser.quit()