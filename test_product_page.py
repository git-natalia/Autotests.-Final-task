from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.links import ProductPageLinks
import pytest
from mimesis import Person

class TestGuestAddToBasketFromProductPage():
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer0",
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer1",
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer2",
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer3",
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer4",
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer5",
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer6",
                                      pytest.param(ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer7", marks=pytest.mark.xfail),
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer8",
                                      ProductPageLinks.LINK_PRODUCT_PAGE + "?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_add_product_to_basket_button()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_in_basket()

    def test_guest_cant_see_success_message(self, browser):
        # Открываем страницу товара
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

class TestMessagesAfterAddingProductToBasket():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        #Добавляем товар в корзину
        page.should_be_add_product_to_basket_button()
        page.add_product_to_basket()
        #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        #Добавляем товар в корзину
        page.should_be_add_product_to_basket_button()
        page.add_product_to_basket()
        #Проверяем, что нет сообщения об успехе с помощью is_disappeared
        page.should_disappear_success_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        user = Person()
        email = user.email()
        password = user.telephone()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_add_product_to_basket_button()
        page.add_product_to_basket()
        page.should_be_product_in_basket()

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        link = ProductPageLinks.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #Гость открывает страницу товара
    link = ProductPageLinks.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    #Переходит в корзину по кнопке в шапке
    page.should_be_look_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_product_in_basket()
    #Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_no_products_in_basket_message()