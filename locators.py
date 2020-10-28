
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REG_FORM = (By.CSS_SELECTOR,"#register_form")
class addCard():
    click = (By.CSS_SELECTOR, '#add_to_basket_form')
    check_selector = (By.CSS_SELECTOR, 'div h1')
    check_selector2 = (By.CSS_SELECTOR,'#messages div:nth-child(1) strong')
    price = (By.CSS_SELECTOR,'.product_page .price_color')
    price2 = (By.CSS_SELECTOR,'#messages div:nth-child(3) strong')