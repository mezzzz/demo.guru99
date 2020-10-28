from .base_page import BasePage
from .locators import addCard


class BuyPage(BasePage):
    def add_to_cartt(self):
        login_links = self.browser.find_element(*addCard.click)
        login_links.click()
