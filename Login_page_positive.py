from selenium import webdriver
import time

link = 'https://the-internet.herokuapp.com/login'
browser = webdriver.Chrome()
browser.get(link)
try:
    username = browser.find_element_by_css_selector('[name="username"]').send_keys('tomsmith')
    password = browser.find_element_by_css_selector('[name="password"]').send_keys('SuperSecretPassword!')
    login = browser.find_element_by_css_selector('[class="fa fa-2x fa-sign-in"]').click()
    welcome = browser.find_element_by_css_selector('[class="subheader"]').text
    welcometext = 'Welcome to the Secure Area. When you are done click logout below.'
    assert welcome == welcometext, f'expected {welcometext}, got {welcome}'
    logout = browser.find_element_by_css_selector('.button.secondary.radius').click()
    loginpage = browser.find_element_by_tag_name('h2').text
    loginok = 'Login Page'
    assert loginok == loginpage, f'expected {loginok}, got {loginpage}'
finally:
    time.sleep(2)
    browser.quit()