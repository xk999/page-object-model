from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click() 
    def added_to_cart_alert_is_present(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_CART), "Added to cart alert is not presented"
    def product_names_match(self):
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_CART).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Product names do not match"
    def cart_total_alert_is_present(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_TOTAL), "Cart total alert is not presented"
    def prices_match(self):
        assert self.browser.find_element(*ProductPageLocators.ALERT_CART_TOTAL).text == self.browser.find_element(*ProductPageLocators.PRICE).text, "Prices do not match"    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_CART), "Success message is presented, but should not be"
    def alert_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_CART), "Success message should disappear"