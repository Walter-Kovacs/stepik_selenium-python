import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language: en, ru, de, ...")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    if not lang is None: #Если параметр language указан, запускаем браузер с этим параметром
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        print("\nstart browser for test (language=" + lang + ")...")
        browser = webdriver.Chrome(options=options)
    else: #Иначе, запускаем без параметра
        print("\nstart browser for test ...")
        browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()
