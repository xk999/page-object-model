from pages.product_page import ProductPage # точка перед pages убрана, т. к. она вызывает ошибку импорта (no known parent package)
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.added_to_cart_alert_is_present()
    page.product_names_match()
    page.cart_total_alert_is_present()
    page.prices_match()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()
 
def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
 
@pytest.mark.xfail(reason="Feature is not implemented yet")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.alert_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):   
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, link) 
        page.open()                 
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        login_page = LoginPage(browser, link) 
        login_page.register_new_user(email) 

    def test_user_cant_see_success_message(self, browser): 
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): 
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        page.added_to_cart_alert_is_present()
        page.product_names_match()
        page.cart_total_alert_is_present()
        page.prices_match()
