import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    num1_elem = browser.find_element_by_id("num1")
    num2_elem = browser.find_element_by_id("num2")
    sum = str(int(num1_elem.text) + int(num2_elem.text))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
    time.sleep(10)

finally:
    browser.quit()
