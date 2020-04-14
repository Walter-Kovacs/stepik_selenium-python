import time
from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()
    assert True
    
    time.sleep(5)

finally:
    browser.quit()