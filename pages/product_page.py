from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_bkt = self.browser.find_element(*ProductPageLocators.btn_add_to_bkt)
        add_to_bkt.click()

    def should_be_add_item_alert(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.item_name), \
            "Item name not presented"
        assert self.is_element_present(*ProductPageLocators.add_txt_msg), \
            "Message about adding is not presented"

        # получаем текст элементов для проверки
        item_name = self.browser.find_element(*ProductPageLocators.item_name).text
        message = self.browser.find_element(*ProductPageLocators.add_txt_msg).text
        assert item_name == message, "Message of add to basket not compare with item name"

    def should_be_price_basket_alert(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.price_item), \
            "Price item not presented"
        assert self.is_element_present(*ProductPageLocators.price_bkt_msg), \
            "Message about price of basket is not presented"

        # получаем текст элементов для проверки
        item_price = self.browser.find_element(*ProductPageLocators.price_item).text
        message_pr_bkt = self.browser.find_element(*ProductPageLocators.price_bkt_msg).text
        assert item_price == message_pr_bkt, "Message of price basket not compare with item price"

    # проверяет, что элемент не появляется на странице в течение заданного времени:
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.add_txt_msg), \
            "Success message is presented, but should not be"

    # проверяем,что какой-то элемент исчезает
    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.add_txt_msg), \
            "Success message is presented, but should not be"


