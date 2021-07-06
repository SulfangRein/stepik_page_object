from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_message(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_TEXT).text == "Your basket is empty. Continue " \
                                                                                 "shopping", "Basket is not empty"
