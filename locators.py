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


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class Empty_Basket():
    link_basket = (By.CSS_SELECTOR, '.btn-group')
    check_empty_basket = (By.CSS_SELECTOR, '#content_inner a') #+ TEXT
    wares_in_basket = (By.CSS_SELECTOR, '#content_inner div .row .col-sm-6 ') #IS ELEMENT NOT PRESENT


class Reg_New_User():
    email = (By.CSS_SELECTOR, "#id_registration-email")
    password = (By.CSS_SELECTOR, "#id_registration-password1")
    confirm_password = (By.CSS_SELECTOR, "#id_registration-password2")
    confirm_click = (By.CSS_SELECTOR, '[value="Register"]')
