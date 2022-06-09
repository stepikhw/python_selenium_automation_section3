import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Specify a language to run browser with")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    # "en-us" language will be used by default
    if browser_language is not None:
        pass
    else:
        browser_language = "en-us"
    print(f"\nStart Chrome browser (language=\"{browser_language}\") for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser..")
    browser.quit()
