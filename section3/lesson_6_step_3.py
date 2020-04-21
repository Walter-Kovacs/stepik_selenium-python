import math
import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser...")
    browser.quit()

@pytest.mark.parametrize('lesson_number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_ufo(browser, lesson_number):
    link = f"https://stepik.org/lesson/{lesson_number}/step/1"
    browser.get(link)
    
    #Input and send answer
    input_element = browser.find_element_by_css_selector(".textarea")
    input_element.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    
    #Check
    feedback_element = browser.find_element_by_css_selector(".smart-hints__hint")
    feedback_text = feedback_element.text
    assert feedback_text == "Correct!", feedback_text
