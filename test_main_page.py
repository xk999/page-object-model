from pages.main_page import MainPage # точка перед pages убрана, т. к. она вызывает ошибку импорта (no known parent package)
from pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser): 
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page() 
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()   

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_forms(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page() 
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    login_page.should_be_register_form()
