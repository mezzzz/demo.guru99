from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import Reg_New_User
import faker
f = faker.Faker()
email = f.email()



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "REG link is not presented"

    def should_be_login_url(self):
        assert "http://selenium1py.pythonanywhere.com/en-gb/accounts/logn/" in self.browser.current_url, "ничего"


    def register_new_user(self,email,password):
        email = self.browser.find_element(*Reg_New_User.email).send_keys(email)
        password = self.browser.find_element(*Reg_New_User.password).send_keys(password)





