from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_products_in_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.NO_PRODUCTS_IN_BASKET_MESSAGE), "No products in basket message is not presented"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket items is presented in error"
