from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    #Заполнение обязательных полей
    input_fields = browser.find_elements_by_css_selector(".first_block input")
    for field in input_fields:
        field.send_keys("txt")
    
    #Отправка заполненной формы
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    #Проверка успешности регистрации
    time.sleep(1) #Ожидание загрузки страницы
    welcome_text_elem = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elem.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    
    time.sleep(10) #Ожидаение для возможности визуальной оценки

finally:
    browser.quit()
