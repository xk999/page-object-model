from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():   
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_PRODUCT_ADDED_TO_CART = (By.XPATH, "//div[1]/div[@class='alertinner ']/strong")
    PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_CART_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
