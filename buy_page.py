from .base_page import BasePage
from .locators import addCard
from .locators import Empty_Basket



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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*addCard.check_selector2), \
            "Success message is presented, but should not be"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*addCard.check_selector2), \
            "Success message is presented, but should not be"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*addCard.check_selector2), \
            "Success message is presented, but should not be"


    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*addCard.check_selector2), \
            "Success message is presented, but should not be"

    def go_to_basket(self):
        find = self.browser.find_element(*Empty_Basket.link_basket)
        find.click()


    def wares_is_not_have(self):
        self.is_not_element_present(*Empty_Basket.wares_in_basket), \
            "Success message is presented, but should not be"


    def basket_is_empty(self):
        basket = self.browser.find_element(*Empty_Basket.check_empty_basket).text
        print(basket)
        assert basket == "Продолжить покупки", "net"
class TestUserAddToBasketFromProductPage(BasePage):
    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = BuyPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    def test_user_add_to_card(browser, link):
        # page = BuyPage(browser)
        page = BuyPage(browser, link)
        page.open()
        page.add_to_cartt()
        page.solve_quiz_and_get_code()
        page.check_name()
        page.check_price()




