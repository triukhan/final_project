from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators


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
        assert self.is_element_present(*LoginPageLocators.UP_PASSWORD_FIELD), "Password field is absent"
        assert self.is_element_present(*LoginPageLocators.UP_CONFIRM_PASSWORD_FIELD), "Confirm password field is absent"
        assert self.is_element_present(*LoginPageLocators.UP_BUTTON), "Button is absent"

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.UP_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.UP_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.UP_CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.click_element(*LoginPageLocators.UP_BUTTON)

    def user_should_be_logged_in(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), 'User is logged out'
