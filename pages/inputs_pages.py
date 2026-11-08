from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class InputsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._text_input = page.get_by_test_id("text-input")
        self._email_input = page.get_by_test_id("email-input")
        self._password_input = page.get_by_test_id("password-input")
        self._password_toggle_button = page.get_by_test_id("password-input-toggle")
        self._number_input = page.get_by_test_id("number-input")
        self._date_input = page.get_by_test_id("date-input")
        self._time_input = page.get_by_test_id("time-input")
        self._search_input = page.get_by_test_id("search-input")
        self._phone_country_button = page.get_by_test_id("phone-country-code")
        self._phone_country_list = page.get_by_test_id("phone-country-list")
        self._phone_prefix = page.get_by_test_id("phone-prefix")
        self._phone_input = page.get_by_test_id("tel-input")
        self._textarea = page.get_by_test_id("textarea-input")
        self._readonly_input = page.get_by_test_id("readonly-input")
        self._disabled_input = page.get_by_test_id("disabled-input")
        self._live_output_input = page.get_by_test_id("input-output")
        self._live_output = page.get_by_test_id("input-output-result")


    def open(self) -> None:
        super().open("#inputs")

    def get_text_input(self) -> Locator:
        return self._text_input

    def get_email_input(self) -> Locator:
        return self._email_input

    def get_password_input(self) -> Locator:
        return self._password_input

    def get_password_toggle_button(self) -> Locator:
        return self._password_toggle_button

    def get_number_input(self) -> Locator:
        return self._number_input

    def get_date_input(self) -> Locator:
        return self._date_input

    def get_time_input(self) -> Locator:
        return self._time_input

    def get_search_input(self) -> Locator:
        return self._search_input

    def get_phone_country_button(self) -> Locator:
        return self._phone_country_button

    def get_phone_country_option(self, country_code: str) -> Locator:
        return self._phone_country_list.get_by_test_id(f"phone-country-{country_code}")

    def get_phone_prefix(self) -> Locator:
        return self._phone_prefix

    def get_phone_input(self) -> Locator:
        return self._phone_input

    def get_textarea(self) -> Locator:
        return self._textarea

    def get_readonly_input(self) -> Locator:
        return self._readonly_input

    def get_disabled_input(self) -> Locator:
        return self._disabled_input

    def get_live_output_input(self) -> Locator:
        return self._live_output_input

    def get_live_output(self) -> Locator:
        return self._live_output
