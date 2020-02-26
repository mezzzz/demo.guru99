from selenium import webdriver
import time

link = 'https://the-internet.herokuapp.com/add_remove_elements/'
browser = webdriver.Chrome()
browser.get(link)
try:
    addclick = browser.find_element_by_css_selector('[onclick="addElement()"]').click()
    time.sleep(2)
    delclick = browser.find_element_by_css_selector('[onclick = "deleteElement()"]').click()
    delclick2 = browser.find_element_by_css_selector('[onclick = "deleteElement()"]').click()
    #Выбросит исключение, что элемента уже нет.
finally:
    time.sleep(2)
    browser.quit()