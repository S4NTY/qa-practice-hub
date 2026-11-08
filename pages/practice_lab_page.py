from datetime import datetime
from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class PracticeLabPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._cookie_consent_dialog = page.get_by_role("dialog").filter(
            has_text="We use cookies"
        )

        self._wizard_name_input = page.get_by_test_id("wizard-name")
        self._wizard_email_input = page.get_by_test_id("wizard-email")
        self._wizard_city_input = page.get_by_test_id("wizard-city")
        self._wizard_zip_input = page.get_by_test_id("wizard-zip")
        self._wizard_message = page.get_by_test_id("wizard-message")
        self._wizard_review = page.get_by_test_id("wizard-review")
        self._wizard_next_button = page.get_by_test_id("wizard-next")
        self._wizard_back_button = page.get_by_test_id("wizard-back")
        self._wizard_submit_button = page.get_by_test_id("wizard-submit")

        self._custom_date_trigger = page.get_by_test_id("custom-date-trigger")
        self._custom_date_picker = page.get_by_test_id("custom-date-picker")
        self._custom_date_value = page.get_by_test_id("custom-date-value")
        self._custom_date_input = page.get_by_test_id("custom-date-input")
        self._custom_date_output = page.get_by_test_id("custom-date-output")
        self._custom_date_month_label = page.get_by_test_id("custom-date-month-label")
        self._custom_date_prev_button = page.get_by_test_id("custom-date-prev")
        self._custom_date_next_button = page.get_by_test_id("custom-date-next")

        self._stale_demo_button = page.get_by_test_id("stale-action-btn")
        self._stale_demo_output = page.get_by_test_id("stale-output")


    def open(self) -> None:
        super().open("#practice-lab")

    def get_wizard_name_input(self) -> Locator:
        return self._wizard_name_input

    def get_wizard_email_input(self) -> Locator:
        return self._wizard_email_input

    def get_wizard_city_input(self) -> Locator:
        return self._wizard_city_input

    def get_wizard_zip_input(self) -> Locator:
        return self._wizard_zip_input

    def get_wizard_message(self) -> Locator:
        return self._wizard_message

    def get_wizard_review(self) -> Locator:
        return self._wizard_review

    def get_wizard_panel(self, step: int) -> Locator:
        return self.page.get_by_test_id(f"wizard-panel-{step}")

    def get_custom_date_picker(self) -> Locator:
        return self._custom_date_picker

    def get_custom_date_value(self) -> Locator:
        return self._custom_date_value

    def get_custom_date_input(self) -> Locator:
        return self._custom_date_input

    def get_custom_date_output(self) -> Locator:
        return self._custom_date_output

    def get_stale_demo_button(self) -> Locator:
        return self._stale_demo_button

    def get_stale_demo_output(self) -> Locator:
        return self._stale_demo_output

    def enter_wizard_personal_details(self, name: str, email: str) -> None:
        self._wizard_name_input.fill(name)
        self._wizard_email_input.fill(email)

    def enter_wizard_address(self, city: str, zip_code: str) -> None:
        self._wizard_city_input.fill(city)
        self._wizard_zip_input.fill(zip_code)

    def go_to_next_wizard_step(self) -> None:
        self._wizard_next_button.click()

    def go_to_previous_wizard_step(self) -> None:
        self._wizard_back_button.click()

    def submit_wizard(self) -> None:
        self._wizard_submit_button.click()

    def select_custom_date(self, date_text: str) -> None:
        target_date = datetime.strptime(date_text, "%Y-%m-%d")
        self._custom_date_trigger.click()
        displayed_month = datetime.strptime(
            self._custom_date_month_label.inner_text(), "%B %Y"
        )
        month_difference = (
            (target_date.year - displayed_month.year) * 12
            + target_date.month
            - displayed_month.month
        )
        month_button = (
            self._custom_date_prev_button
            if month_difference < 0
            else self._custom_date_next_button
        )
        for _ in range(abs(month_difference)):
            month_button.click()
        self._custom_date_picker.get_by_role(
            "button", name=str(target_date.day), exact=True
        ).click()

    def click_stale_demo(self, times: int = 1) -> None:
        for _ in range(times):
            self._stale_demo_button.click()
