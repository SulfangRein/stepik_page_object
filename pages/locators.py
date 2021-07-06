from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_PRICE = (By.CSS_SELECTOR, '.alert-success')
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success strong')


class BasketPageLocators:
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
