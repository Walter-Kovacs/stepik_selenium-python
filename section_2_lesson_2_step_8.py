import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    #name, last name, e-mail
    elem_css_selectors = ["[name='firstname']", "[name='lastname']", "[name='email']"]
    for slector in elem_css_selectors:
        elem = browser.find_element_by_css_selector(slector)
        elem.send_keys("txt")
    
    #load file
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "textFile.txt")
    load_file_elem = browser.find_element_by_id("file")
    load_file_elem.send_keys(file_path)
    
    #submit
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
    
    time.sleep(10)

finally:
    browser.quit()
