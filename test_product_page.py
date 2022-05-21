from pages.product_page import ProductPage # точка перед pages убрана, т. к. она вызывает ошибку импорта (no known parent package)
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.added_to_cart_alert_is_present()
    page.product_names_match()
    page.cart_total_alert_is_present()
    page.prices_match()
    #time.sleep(10)