import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button = browser.find_element_by_id("book")
    book_button.click()
    
    #Считывание значения x и вычисление выражения
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    #Ввод ответа в текстовое поле
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)
    #Нажатие кнопки
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
    
    time.sleep(10)

finally:
    browser.quit()
