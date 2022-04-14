from .main_page import MainPage
from .locators import CartPageLocators

class BasketPageMethods(MainPage):

    def check_if_the_cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.CART_CONTAINS_SOME_ELEMENTS)

    def check_if_the_message_on_absence_is_present(self):
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY)


