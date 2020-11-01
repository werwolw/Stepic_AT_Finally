from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Link not increase 'link'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Reg-form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.email_input)
        input_email.send_keys(email)
        input_pass = self.browser.find_element(*LoginPageLocators.password_input)
        input_pass.send_keys(password)
        input_pass_conf = self.browser.find_element(*LoginPageLocators.password_input_confirm)
        input_pass_conf.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.button_register)
        button_register.click()
