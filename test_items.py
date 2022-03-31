from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

class General():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def quit(self):
        self.browser.quit()

class LocatorForTheButton():
    button = (By.CSS_SELECTOR, "#login_link")

class SearchingMechanism(General):

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_the_button(self):
        assert self.is_element_present(*LocatorForTheButton.button), 'The button is not here'

def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = SearchingMechanism(browser, link)
        page.open()
        time.sleep(30)
        page.should_be_the_button()

