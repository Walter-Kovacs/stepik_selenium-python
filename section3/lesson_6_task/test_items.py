import pytest
import time
from selenium.webdriver.remote.errorhandler import NoSuchElementException

def test_add_to_basket_button_existence(browser):
    try:
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        #time.sleep(30)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        button_exist = True
    except NoSuchElementException:
        button_exist = False
    
    assert button_exist, "Button for add to basket does not exist!"
