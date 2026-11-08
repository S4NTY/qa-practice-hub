from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class AlertsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._alert_button = page.get_by_test_id("btn-alert")
        self._confirm_button = page.get_by_test_id("btn-confirm")
        self._prompt_button = page.get_by_test_id("btn-prompt")
        self._validated_prompt_button = page.get_by_test_id("btn-prompt-validated")
        self._toast_button = page.get_by_test_id("btn-show-toast")
        self._alert_output = page.get_by_test_id("alert-output")
        self._toast_message = page.get_by_test_id("toast-message")


    def open(self) -> None:
        super().open("#alerts")

    def get_alert_output(self) -> Locator:
        return self._alert_output

    def get_toast_message(self) -> Locator:
        return self._toast_message

    def show_alert(self) -> None:
        self._alert_button.click()

    def show_confirm(self) -> None:
        self._confirm_button.click()

    def show_prompt(self) -> None:
        self._prompt_button.click()

    def show_validated_prompt(self) -> None:
        self._validated_prompt_button.click()

    def show_toast(self) -> None:
        self._toast_button.click()
