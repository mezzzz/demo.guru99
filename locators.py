from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REG_FORM = (By.CSS_SELECTOR,"#register_form")
class addCard():
    click = (By.CSS_SELECTOR, '#add_to_basket_form')