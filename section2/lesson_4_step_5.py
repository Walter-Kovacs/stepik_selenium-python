import time
from selenium import webdriver

link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get(link)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text
    
    time.sleep(3)

finally:
    browser.quit()
