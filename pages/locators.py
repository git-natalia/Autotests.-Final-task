from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOOK_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

class BasketPageLocators():
    NO_PRODUCTS_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class MainPageLocators():
    pass
#    LOGIN_LINK = (By.ID, "login_link")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_COST_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")