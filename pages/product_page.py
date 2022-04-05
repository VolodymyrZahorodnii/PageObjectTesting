from .base_page import BasePage
from .main_page import MainPage
from .locators import ProductPageLocators

class ProductPageMethods(MainPage):
    def adding_an_item_to_the_basket(self):
        button = self.browser.find_element_by_css_selector(".btn-add-to-basket")
        button.click()

    def check_if_an_item_added_to_the_basket(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_TO_THE_CART)

    def check_the_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE)

    def check_if_both_namings_match(self):
        naming_on_personal_page = self.browser.find_element_by_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1')
        naming_on_cart_page = self.browser.find_element_by_xpath('//*[@id="messages"]/div[1]/div/strong')
        assert naming_on_personal_page.text == naming_on_cart_page.text, 'Namings do not match'

    def check_if_price_is_okay(self):
        price_on_personal_page = self.browser.find_element_by_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
        price_on_cart_page = self.browser.find_element_by_xpath('//*[@id="messages"]/div[3]/div/p[1]/strong')
        assert price_on_personal_page.text == price_on_cart_page.text, 'Prices do not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_TO_THE_CART), "Success message is presented, but should not be"

    def message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDED_TO_THE_CART), "Success message has not disappeared, but should have"




