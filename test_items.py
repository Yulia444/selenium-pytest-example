import pytest
from selenium import webdriver
import time

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_if_button_buy_on_page_is_available(browser):
    browser.get(LINK)
    #  time.sleep(30)
    xpath_selector = '//form[@id="add_to_basket_form"]/button[@class="btn btn-lg btn-primary btn-add-to-basket"]'
    add_to_basket = browser.find_element_by_xpath(xpath_selector)
    assert add_to_basket != None
