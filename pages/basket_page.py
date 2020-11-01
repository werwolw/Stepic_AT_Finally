from pages.locators import BasketPageLokators
from pages.base_page import BasePage


class BasketPage(BasePage):
    # проверка, что корзина пустая
    def should_be_empty_basket_message(self):
        # получаем текст элемента для проверки
        empty_message_txt = self.browser.find_element(*BasketPageLokators.empty_basket_text).text
        assert "empty" in empty_message_txt, \
            "Message of empty basket not presented or basket not empty"

    # проверяем, что кнопка "Перейти к оформлению" не появляется на странице
    # в течение заданного времени:
    def should_not_be_button_proceed_checkout(self):
        assert self.is_not_element_present(*BasketPageLokators.btn_prcd_to_checkout), \
            "Checkout button is presented, but should not be"
