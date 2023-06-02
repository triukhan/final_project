from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login"), "Cant find word login in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.IN_LOGIN_FIELD), "Login field is absent"
        assert self.is_element_present(*LoginPageLocators.IN_PASSWORD_FIELD), "Password field is absent"
        assert self.is_element_present(*LoginPageLocators.IN_BUTTON), "Button is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.UP_EMAIL_FIELD), "Email field is absent"
        assert self.is_element_present(*LoginPageLocators.IN_PASSWORD_FIELD), "Password field is absent"
        assert self.is_element_present(*LoginPageLocators.UP_CONFIRM_PASSWORD_FIELD), "Confirm password field is absent"
        assert self.is_element_present(*LoginPageLocators.UP_BUTTON), "Button is absent"
