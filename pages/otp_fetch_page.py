from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class OTPFetchPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.otp_fetch_title_label = page.get_by_test_id("otp-fetch-title")
        self.otp_display_label = page.locator("#otp-display")
        self.otp_close_countdown_label = page.locator("#otp-close-countdown")


    def open(self) -> None:
        super().open("otp-fetch.html")

    def get_otp_fetch_title_label(self) -> Locator:
        return self.otp_fetch_title_label

    def get_otp_display_label(self) -> Locator:
        return self.otp_display_label

    def get_otp_close_countdown_label(self) -> Locator:
        return self.otp_close_countdown_label

    def otp_display_label_get_text(self) -> str:
        return self.otp_display_label.text_content()

    def get_otp_close_countdown_value(self) -> str:
        return self.otp_close_countdown_label.text_content()
