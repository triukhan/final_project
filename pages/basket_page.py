from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_go_basket_and_see_empty_text(self):
        self.should_be_text_in_basket()
        self.should_be_empty_text()

    def should_be_text_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT)

    def should_be_empty_text(self):
        print(self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text)
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text == 'Your basket is empty. ' \
               'Continue shopping', 'Basket is not empty'
