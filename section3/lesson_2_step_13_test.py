from selenium import webdriver
import time
import unittest

class TestFindElements(unittest.TestCase):
    def run_on_link(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        
        #Заполнение обязательных полей
        css_selectors_lst = [".first_block input.first", ".first_block input.second", ".first_block input.third"]
        for selector in css_selectors_lst:
            field_input = browser.find_element_by_css_selector(selector)
            field_input.send_keys("txt")
        
        #Отправка заполненной формы
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        #Возврат текста успешности регистрации
        time.sleep(1) #Ожидание загрузки страницы
        welcome_text = browser.find_element_by_tag_name("h1").text
        browser.quit()
        return welcome_text
    
    def test_link1(self):
        welcome_text = self.run_on_link("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Somthing wrong.")
    
    def test_link2(self):
        welcome_text = self.run_on_link("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Somthing wrong.")

if __name__ == "__main__":
    unittest.main()
