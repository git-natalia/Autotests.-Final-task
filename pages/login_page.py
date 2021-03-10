from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_register_fields()
        self.should_be_register_submit_button()
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        registration_email.send_keys(email)
        registration_password1.send_keys(password)
        registration_password2.send_keys(password)
        registration_submit_button.click()

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "/login/" in self.browser.current_url, "Login page URL is not correct"

    def should_be_register_field_email(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Register form field for email is not presented"

    def should_be_register_fields(self):
        self.should_be_register_field_email()
        self.should_be_register_field_password1()
        self.should_be_register_field_password2()

    def should_be_register_field_password1(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Register form field for password is not presented"

    def should_be_register_field_password2(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Register form field for confirm password is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_register_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), "Register submit button is not presented"



