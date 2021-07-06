from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()
        self.should_be_product_price_equals_basket_price()
        self.should_be_product_name_equals_name_in_success_message()

    def should_be_product_name_equals_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_price = self.browser.find_element(*ProductPageLocators.SUCCESS_PRICE).text
        assert product_name == success_price, "Product name not equals in success message"

    def should_be_product_price_equals_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        assert product_price == total_price, "Product price not equals total price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT)

