from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class OTPResendPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._otp_display_label = page.locator("#otp-display")
        self._otp_resend_title_label = page.get_by_test_id("otp-resend-title")


    def open(self) -> None:
        super().open("otp-resend.html")

    def get_otp_resend_title_label(self) -> Locator:
        return self._otp_resend_title_label

    def otp_display_label_get_text(self) -> str:
        return self._otp_display_label.text_content()
