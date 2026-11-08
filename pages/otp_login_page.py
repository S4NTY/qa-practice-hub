from pages.base_page import BasePage
from playwright.sync_api import Page, Locator
from pages.otp_fetch_page import OTPFetchPage
from pages.otp_resend_page import OTPResendPage


class OTPLoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._otp_username_input = page.locator("#otp-username")
        self._otp_fetch_button = page.locator("#btn-fetch-otp")
        self._otp_resend_button = page.locator("#btn-resend-otp")
        self._otp_login_message_label = page.locator("#otp-login-message")


    def open(self) -> None:
        super().open("#otp-login")

    def get_otp_login_message_label(self) -> Locator:
        return self._otp_login_message_label

    def get_otp_fetch_button(self) -> Locator:
        return self._otp_fetch_button

    def get_otp_resend_button(self) -> Locator:
        return self._otp_resend_button

    def otp_username_input_set_text(self, text: str) -> None:
        self._otp_username_input.fill(text)

    def otp_fetch_button_click(self) -> OTPFetchPage:
        return OTPFetchPage(self._click_and_catch_popup(self._otp_fetch_button))

    def otp_resend_button_click(self) -> OTPResendPage:
        return OTPResendPage(self._click_and_catch_popup(self._otp_resend_button))

    def set_one_time_password(self, code: str) -> None:
        for i in range(1, 7):
            input_element = self.page.get_by_test_id(f"otp-digit-{i}")
            input_element.fill(code[i-1])

    def _click_and_catch_popup(self, button: Locator) -> Page:
        with self.page.expect_popup() as popup_info:
            button.click()
        popup = popup_info.value
        popup.wait_for_load_state("domcontentloaded")
        return popup
