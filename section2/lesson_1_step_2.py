from selenium import webdriver
import time

link = "file:///D:/coding.edu/SeleniumStepik/test.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(5)
    option1 = browser.find_element_by_css_selector("[for='java']")
    option1.click()
    time.sleep(5)

finally:
    browser.quit()
