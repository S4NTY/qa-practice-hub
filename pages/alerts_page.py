from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class AlertsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.alert_button = page.get_by_test_id("btn-alert")
        self.confirm_button = page.get_by_test_id("btn-confirm")
        self.prompt_button = page.get_by_test_id("btn-prompt")
        self.validated_prompt_button = page.get_by_test_id("btn-prompt-validated")
        self.toast_button = page.get_by_test_id("btn-show-toast")
        self.alert_output = page.get_by_test_id("alert-output")
        self.toast_message = page.get_by_test_id("toast-message")


    def open(self) -> None:
        super().open("#alerts")

    def get_alert_output(self) -> Locator:
        return self.alert_output

    def get_toast_message(self) -> Locator:
        return self.toast_message

    def show_alert(self) -> None:
        self.alert_button.click()

    def show_confirm(self) -> None:
        self.confirm_button.click()

    def show_prompt(self) -> None:
        self.prompt_button.click()

    def show_validated_prompt(self) -> None:
        self.validated_prompt_button.click()

    def show_toast(self) -> None:
        self.toast_button.click()
