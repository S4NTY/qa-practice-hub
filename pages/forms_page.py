from playwright.sync_api import Locator
from pages.base_page import BasePage


class FormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._login_username_input = page.locator("#login-username")
        self._login_password_input = page.locator("#login-password")
        self._login_message_label = page.locator("#login-message")
        self._forgot_username_input = page.locator("#forgot-username")
        self._forgot_password_result_label = page.locator("#forgot-password-result")
        self._forgot_password_message_label = page.locator("#forgot-password-message")
        self._reg_firstname_input = page.locator("#reg-firstname")
        self._reg_lastname_input = page.locator("#reg-lastname")
        self._reg_email_input = page.locator("#reg-email")
        self._reg_country_select = page.locator("#reg-country")
        self._reg_message_label = page.locator("#register-message")


    def open(self) -> None:
        super().open("#forms")

    def get_login_message_label(self) -> Locator:
        return self._login_message_label

    def get_forgot_password_result_label(self) -> Locator:
        return self._forgot_password_result_label

    def get_forgot_password_message_label(self) -> Locator:
        return self._forgot_password_message_label

    def get_reg_message_label(self) -> Locator:
        return self._reg_message_label

    def login_username_input_set_text(self, text: str) -> None:
        self._login_username_input.fill(text)

    def login_password_input_set_text(self, text: str) -> None:
        self._login_password_input.fill(text)

    def forgot_username_input_set_text(self, text: str) -> None:
        self._forgot_username_input.fill(text)

    def reg_firstname_input_set_text(self, text: str) -> None:
        self._reg_firstname_input.fill(text)

    def reg_lastname_input_set_text(self, text: str) -> None:
        self._reg_lastname_input.fill(text)

    def reg_email_input_set_text(self, text: str) -> None:
        self._reg_email_input.fill(text)

    def reg_country_select_by_text(self, text: str) -> None:
        self._reg_country_select.select_option(text)

    def is_registration_form_empty(self) -> bool:
        return (
            self._reg_firstname_input.input_value() == ""
            and self._reg_lastname_input.input_value() == ""
            and self._reg_email_input.input_value() == ""
            and self._reg_country_select.input_value() == ""
        )
