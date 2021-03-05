from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def add_product_to_basket(self):
        # добавление в корзину
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_product_in_basket(self):
        self.should_be_product_name()
        self.should_be_product_name_in_message()
        self.should_be_product_name_in_message_equal_product_name()
        self.should_be_product_cost()
        self.should_be_basket_cost_in_message()
        self.should_be_basket_cost_in_message_equal_product_cost()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_name_in_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Product name is not presented in message"

    def should_be_product_name_in_message_equal_product_name(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_message == product_name, "Product name in message is not equal product name"

    def should_be_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), "Product cost is not presented"

    def should_be_basket_cost_in_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_IN_MESSAGE), "Basket cost is not presented in message"

    def should_be_basket_cost_in_message_equal_product_cost(self):
        basket_cost_in_message = self.browser.find_element(*ProductPageLocators.BASKET_COST_IN_MESSAGE).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        assert basket_cost_in_message == product_cost, "Basket cost in message is not equal product cost"

