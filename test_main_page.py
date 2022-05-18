from pages.main_page import MainPage # точка перед pages убрана, т. к. она вызывает ошибку импорта (no known parent package)

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser): 
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()     
