import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.buy_page import BuyPage
from pages.base_page import BasePage
import math
import time

def test_guest_cant_see_product_in_basket_opened_from_product_page():
