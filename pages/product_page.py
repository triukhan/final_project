from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.product_name = None
        self.massage_name = None
        self.product_price = None

    def should_be_added_to_page(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_add_button()
        self.should_product_added()
        self.solve_quiz_and_get_code()
        self.should_appear_successful_message()
        self.should_appear_total_alert()

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "The product name is absent"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "The product price is absent"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRICE).text

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "The button is absent"

    def should_product_added(self):
        assert self.click_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "The button is not clickable"

    def should_appear_successful_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_ALERT), "The successful alert is absent"
        self.message_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert self.message_name == self.product_name

    def should_appear_total_alert(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "The total alert is absent"
        self.message_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert self.product_price == self.message_price, "The price in the alert doesn't match with price" \
                                                         " on the product"
        print(self.message_price, self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_ALERT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_ALERT), \
            "Success message is presented, but should not be"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

