from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    IN_LOGIN_FIELD = (By.NAME, "login-username")
    IN_PASSWORD_FIELD = (By.NAME, "login-password")
    IN_BUTTON = (By.NAME, "login_submit")

    UP_EMAIL_FIELD = (By.NAME, "registration-email")
    UP_PASSWORD_FIELD = (By.NAME, "registration-password1")
    UP_CONFIRM_PASSWORD_FIELD = (By.NAME, "id_registration-password2")
    UP_BUTTON = (By.NAME, "registration_submit")

