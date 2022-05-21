from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click() 
    def added_to_cart_alert_is_present(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_CART), "Added to cart alert is not presented"
    def product_names_match(self):
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_ADDED_TO_CART).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Product names do not match"
    def cart_total_alert_is_present(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_TOTAL), "Basket updated total alert is not presented"
    def prices_match(self):
        assert self.browser.find_element(*ProductPageLocators.ALERT_CART_TOTAL).text == self.browser.find_element(*ProductPageLocators.PRICE).text, "Prices do not match"    

