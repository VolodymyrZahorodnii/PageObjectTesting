from .pages.main_page import MainPage
from .pages.product_page import ProductPageMethods
from .pages.locators import CartPageLocators
from .pages.basket_page import BasketPageMethods
import time


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_the_page()


    def test_guest_should_see_login_link(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPageMethods(browser, link)
    page.open()
    page.go_to_the_cart()
    page.check_if_the_cart_is_empty()
    page.check_if_the_message_on_absence_is_present()







