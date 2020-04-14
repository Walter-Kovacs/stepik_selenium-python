import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for elem in elements:
        elem.send_keys("txt")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(30)

finally:
    browser.quit()
