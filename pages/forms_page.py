from playwright.sync_api import Locator
from pages.base_page import BasePage


class FormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_username_input = page.locator("#login-username")
        self.login_password_input = page.locator("#login-password")
        self.login_message_label = page.locator("#login-message")
        self.forgot_username_input = page.locator("#forgot-username")
        self.forgot_password_result_label = page.locator("#forgot-password-result")
        self.forgot_password_message_label = page.locator("#forgot-password-message")
        self.reg_firstname_input = page.locator("#reg-firstname")
        self.reg_lastname_input = page.locator("#reg-lastname")
        self.reg_email_input = page.locator("#reg-email")
        self.reg_country_select = page.locator("#reg-country")
        self.reg_message_label = page.locator("#register-message")


    def open(self) -> None:
        super().open("#forms")

    def get_login_message_label(self) -> Locator:
        return self.login_message_label

    def get_forgot_password_result_label(self) -> Locator:
        return self.forgot_password_result_label

    def get_forgot_password_message_label(self) -> Locator:
        return self.forgot_password_message_label

    def get_reg_message_label(self) -> Locator:
        return self.reg_message_label

    def login_username_input_set_text(self, text: str) -> None:
        self.login_username_input.fill(text)

    def login_password_input_set_text(self, text: str) -> None:
        self.login_password_input.fill(text)

    def forgot_username_input_set_text(self, text: str) -> None:
        self.forgot_username_input.fill(text)

    def reg_firstname_input_set_text(self, text: str) -> None:
        self.reg_firstname_input.fill(text)

    def reg_lastname_input_set_text(self, text: str) -> None:
        self.reg_lastname_input.fill(text)

    def reg_email_input_set_text(self, text: str) -> None:
        self.reg_email_input.fill(text)

    def reg_country_select_by_text(self, text: str) -> None:
        self.reg_country_select.select_option(text)

    def is_registration_form_empty(self) -> bool:
        return (
            self.reg_firstname_input.input_value() == ""
            and self.reg_lastname_input.input_value() == ""
            and self.reg_email_input.input_value() == ""
            and self.reg_country_select.input_value() == ""
        )
