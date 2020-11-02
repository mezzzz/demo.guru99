import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.buy_page import BuyPage
from pages.base_page import BasePage
import math
import time
import faker

f = faker.Faker()
email = f.email()
password = "123"

"""
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link() #смотрим присутсвие элемента

def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form() #смотрим присутсвие элемента

def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form() #смотрим присутсвие элемента

def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()  # смотрим присутсвие элемента


def test_add_to_card(browser,link):
    #page = BuyPage(browser)
    page = BuyPage(browser, link)
    page.open()
    page.add_to_cartt()
    page.solve_quiz_and_get_code()
    page.check_name()
    page.check_price()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BuyPage(browser,link)
    page.open()
    #time.sleep(3)
    page.add_to_cartt()
    #time.sleep(3)
    page.guest_cant_see_success_message_after_adding_product_to_basket()
    #time.sleep(3)



def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BuyPage(browser,link)
    page.open()
    time.sleep(3)
    page.guest_cant_see_success_message()
    time.sleep(3)
#100% PASS

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BuyPage(browser,link)
    page.open()
    page.add_to_cartt()
    page.guest_cant_see_success_message()
    
    


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BuyPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BuyPage(browser, link)
    page.open()
    page.go_to_login_page()



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link ="http://selenium1py.pythonanywhere.com"
    page = BuyPage(browser, link)
    page.open()
    page.go_to_basket()
    time.sleep(3)
    page.wares_is_not_have()    #Нет товаров
    page.basket_is_empty()  #Корзина пуста

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link ="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BuyPage(browser, link)
    page.open()
    page.go_to_basket()
    page.wares_is_not_have()
    page.basket_is_empty()


@pytest.mark.login
class TestRegistration():
    @pytest.fixture(scope="function", autouse=True)


def test_registration(browser):
    link ="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user('em,ail','djiguryadas12')
    time.sleep(3)

"""
@pytest.mark.register
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.email = f.email()
        self. password = f.email()
        yield
    def test_registration(self,browser):
        link ="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        time.sleep(3)
