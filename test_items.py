import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_to_basket_button(browser):
    browser.get(link)
    try:
        button = browser.find_element_by_css_selector('#add_to_basket_form button[type="submit"]')
    except selenium.common.exceptions.NoSuchElementException as e:
        assert False, 'Кнопка не найдена'
