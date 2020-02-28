from selenium import webdriver
import time

link = 'https://the-internet.herokuapp.com/checkboxes'
browser = webdriver.Chrome()
browser.get(link)
try:
    input1 = browser.find_element_by_css_selector('#checkboxes [type="checkbox"]:nth-child(3)')
    atr = input1.get_attribute('checked')
    input1.click()
    assert atr is not None, "Чекбокс заполнен"
    input2 = browser.find_element_by_css_selector('#checkboxes [type="checkbox"]:nth-child(1)')
    atr1 = input2.get_attribute('checked')
    assert atr1 is None, "Чекбокс не заполнен"
finally:
    time.sleep(2)
    browser.quit()
    