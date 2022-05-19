from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 
        # return LoginPage(browser=self.browser, url=self.browser.current_url) 
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"    