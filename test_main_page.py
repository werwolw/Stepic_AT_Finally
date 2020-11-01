from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # проверка перехода на страницу логина с главной страницы
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                     # открываем страницу
        page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)    # Инициализируем другую страницу
        login_page.should_be_login_page()   # выполняем проверки из метода should_be_login_page

    # проверка на наличие кнопки логина
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


# проверка пустой корзины при переходе с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_empty_basket_message()
    # проверяем, что кнопка "Перейти к оформлению" не появляется на странице
    # в течение заданного времени:
    page.should_not_be_button_proceed_checkout()
