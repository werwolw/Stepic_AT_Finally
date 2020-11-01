from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    email_input = (By.CSS_SELECTOR, "#id_registration-email")
    password_input = (By.CSS_SELECTOR, "#id_registration-password1")
    password_input_confirm = (By.CSS_SELECTOR, "#id_registration-password2")
    button_register = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators:
    btn_add_to_bkt = (By.CSS_SELECTOR, ".btn-add-to-basket")
    item_name = (By.CSS_SELECTOR, ".product_main h1")
    price_item = (By.CSS_SELECTOR, ".product_main .price_color")
    add_txt_msg = (By.CSS_SELECTOR, ".alertinner strong")
    price_bkt_msg = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators:
    login_link = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    basket_button = (By.CSS_SELECTOR, ".basket-mini .btn-default")
    user_icon = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLokators:
    empty_basket_text = (By.CSS_SELECTOR, "#content_inner")
    btn_prcd_to_checkout = (By.CSS_SELECTOR, ".btn-block") # кнопка Перейти к оформлению
