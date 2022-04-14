import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPageMethods
from .pages.product_page import ProductPageLocators
import time
import math
from .pages.basket_page import BasketPageMethods


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup():
        link = "http://selenium1py.pythonanywhere.com"
        page = ProductPageMethods(browser, link)
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPageMethods(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasketPageMethods(browser, link)
        page.open()
        page.go_to_the_cart()
        page.check_if_the_cart_is_empty()
        page.check_if_the_message_on_absence_is_present()




# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])
# def test_guest_can_add_product_to_basket(browser,link):
#     page = ProductPageMethods(browser, link)
#     page.open()
#     page.adding_an_item_to_the_basket()
#     time.sleep(2)
#     # page.solve_quiz_and_get_code()
#     page.check_if_both_namings_match()
#     page.check_if_price_is_okay()
#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPageMethods(browser, link)
#     page.open()
#     page.adding_an_item_to_the_basket()
#     page.should_not_be_success_message()
#

#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPageMethods(browser, link)
#     page.open()
#     page.adding_an_item_to_the_basket()
#     page.message_should_disappear()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPageMethods(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPageMethods(browser, link)
#     page.open()
#     page.go_to_login_page()










