
from .base_page import BasePage
from .locators import addCard

class BuyPage(BasePage):
    def check_name(self):
        check = self.browser.find_element(*addCard.check_selector).text
        check2 = self.browser.find_element(*addCard.check_selector2).text
        assert check == check2,'НАЗВАНИЕ'
        print(check2)
        print(check)
    def check_price(self):
        check_price = self.browser.find_element(*addCard.price).text
        check_price2 = self.browser.find_element(*addCard.price2).text
        assert check_price ==check_price2, 'Цена отличается'
        print(check_price2)
        print(check_price)
    def add_to_cartt(self):
        login_links = self.browser.find_element(*addCard.click)
        login_links.click()