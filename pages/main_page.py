from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_the_page(self):
        link = self.browser.find_element_by_css_selector("#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_authorization_page(self):
        authorization_link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        authorization_link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True