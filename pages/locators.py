from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
    CART_BUTTON = (By.CSS_SELECTOR, '.btn-group .btn.btn-default')
    EMAIL_FIELD = (By.ID, 'id_registration-email')
    PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REPEAT_PASSWORD_FIELD = (By.ID, 'id_registration-password2')


class ProductPageLocators():
    NAMING_OF_BOOK = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    ITEM_ADDED_TO_THE_CART = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    NAMING_OF_ITEM_IN_CART = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    CART_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div')
    PRICE_OF_BOOK = (By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRICE_OF_CART = (By.XPATH,'//*[@id="messages"]/div[3]/div/p[1]/strong')


class CartPageLocators():
    CART_IS_EMPTY = (By.CSS_SELECTOR,'#content_inner > p')
    CART_CONTAINS_SOME_ELEMENTS = (By.CSS_SELECTOR,'.thumbnail')




