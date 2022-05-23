from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass

class LoginPageLocators():   
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD1 = (By.ID, "id_registration-password1")
    PASSWORD_FIELD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_PRODUCT_ADDED_TO_CART = (By.XPATH, "//div[1]/div[@class='alertinner ']/strong")
    PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_CART_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(., 'Your basket is empty')]")
