import math
import time
from selenium import webdriver

def f_str(x):
    return str(math.log(abs(12*math.sin(float(x))), math.e))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    #Нажатие кнопки перехода и кнопки в модальном окне
    go_to_button = browser.find_element_by_tag_name("button")
    go_to_button.click()
    browser.switch_to.alert.accept()
    
    #Нахождение x и вычисление значения функции
    x = browser.find_element_by_id("input_value").text
    y = f_str(x)
    
    #Submit
    input_elem = browser.find_element_by_id("answer")
    input_elem.send_keys(y)
    browser.find_element_by_css_selector("button.btn[type='submit']").click()
    
    time.sleep(10)

finally:
    browser.quit()
