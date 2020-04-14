from selenium import webdriver
import time

text_for_input = '''Введите номер ссылки:
1 для http://suninjuly.github.io/registration1.html
2 для http://suninjuly.github.io/registration2.html
Запустить тест для ссылки №:'''
link_no = input(text_for_input)

if link_no == '1':
    link = "http://suninjuly.github.io/registration1.html"
elif link_no == '2':
    link = "http://suninjuly.github.io/registration2.html"
else:
    print("Выход без запуска теста.")
    exit()

print("Тест запущен.")
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    #Заполнение обязательных полей
    css_selectors_lst = [".first_block input.first", ".first_block input.second", ".first_block input.third"]
    for selector in css_selectors_lst:
        field_input = browser.find_element_by_css_selector(selector)
        field_input.send_keys("txt")
    
    #Отправка заполненной формы
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    #Проверка успешности регистрации
    time.sleep(1) #Ожидание загрузки страницы
    welcome_text_elem = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elem.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    
    time.sleep(5) #Ожидаение для возможности визуальной оценки

finally:
    browser.quit()
