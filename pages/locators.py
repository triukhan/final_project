from selenium.webdriver.common.by import By


class MainPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span a.btn-default')


class LoginPageLocators:
    IN_LOGIN_FIELD = (By.NAME, "login-username")
    IN_PASSWORD_FIELD = (By.NAME, "login-password")
    IN_BUTTON = (By.NAME, "login_submit")

    UP_EMAIL_FIELD = (By.NAME, "registration-email")
    UP_PASSWORD_FIELD = (By.NAME, "registration-password1")
    UP_CONFIRM_PASSWORD_FIELD = (By.NAME, "registration-password2")
    UP_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '[value="Add to basket"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    SUCCESSFUL_ALERT = (By.CSS_SELECTOR, 'div.alert-success')
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alert-info div p strong')
    BASKET_NAME = (By.CSS_SELECTOR, 'div.alert div strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span a.btn-default')


class BasketPageLocators():
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
