import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_item_have_button_put_in_basket(browser):
    browser.get(link)
    #тут уже есть  time.sleep(30) -->
    time.sleep(30)
    button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert button.get_attribute('type') == 'submit', 'Не та кнопка (!)'
