import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "file:///D:/coding.edu/SeleniumStepik/test.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(4)").click()
    
    checkbox = browser.find_element_by_id("checkbox_abc")
    checkbox.click()
    time.sleep(3)
    
    #Использование Select
    select = Select(browser.find_element_by_tag_name("select"))
    
    select.select_by_value("1")
    time.sleep(3)
    
    select.select_by_visible_text("Java")
    time.sleep(3)
    
    select.select_by_index(0)
    time.sleep(3)

finally:
    browser.quit()
