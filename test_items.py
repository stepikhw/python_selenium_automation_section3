import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Written for using assert only...
def check_if_element_exists(browser, element):
    try:
        # Waiting for 15 seconds for appearing the element on the DOM of a page.
        WebDriverWait(browser, 15).until(EC.presence_of_element_located(element))
        return True
    except:
        return False


def test_if_add_to_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    add_to_basket_btn_selector = (By.CSS_SELECTOR, "button.btn-primary.btn-add-to-basket")
    browser.get(link)
    add_to_basket_button_exists = check_if_element_exists(browser, add_to_basket_btn_selector)
    assert True == add_to_basket_button_exists, "\"Add to basket\" button does not exist."
    # 30 seconds interval to check manually that opened page has expected language
    # Uncomment line below to do this
    # time.sleep(30)
