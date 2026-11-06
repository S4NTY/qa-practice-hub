from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class DynamicPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_item_button = page.get_by_test_id("btn-add-element")
        self.dynamic_items = page.get_by_test_id("dynamic-list").locator("li")
        self.remove_item_button = page.get_by_test_id("btn-remove-element")
        self.load_data_button = page.get_by_test_id("btn-load-data")
        self.loading_spinner = page.get_by_test_id("loading-spinner")
        self.loaded_data = page.get_by_test_id("loaded-data")
        self.delay_input = page.get_by_test_id("delay-input")
        self.custom_delay_button = page.get_by_test_id("btn-custom-delay")
        self.custom_delay_result = page.get_by_test_id("custom-delay-result")
        self.practice_frame = page.frame_locator('[data-testid="practice-iframe"]')
        self.iframe_name = self.practice_frame.get_by_test_id("iframe-name")
        self.iframe_email = self.practice_frame.get_by_test_id("iframe-email")
        self.iframe_role = self.practice_frame.get_by_test_id("iframe-role")
        self.iframe_message_input = self.practice_frame.get_by_test_id("iframe-message")
        self.iframe_submit_button = self.practice_frame.get_by_test_id("iframe-submit")
        self.iframe_clear_button = self.practice_frame.get_by_test_id("iframe-clear")
        self.iframe_form_message = self.practice_frame.get_by_test_id("iframe-message-box")
        self.iframe_text_toggle_button = self.practice_frame.get_by_test_id("iframe-toggle-text")
        self.iframe_hidden_text = self.practice_frame.get_by_test_id("iframe-hidden-text")


    def open(self) -> None:
        super().open("#dynamic")

    def get_dynamic_items(self) -> Locator:
        return self.dynamic_items

    def get_loading_spinner(self) -> Locator:
        return self.loading_spinner

    def get_custom_delay_result(self) -> Locator:
        return self.custom_delay_result

    def get_tab_button(self, tab: str) -> Locator:
        return self.page.get_by_test_id(f"tab-btn-{tab.lower()}")

    def get_tab_panel(self, tab: str) -> Locator:
        return self.page.get_by_test_id(f"tab-panel-{tab.lower()}")

    def get_loaded_data(self) -> Locator:
        return self.loaded_data

    def get_iframe_hidden_text(self) -> Locator:
        return self.iframe_hidden_text

    def get_iframe_form_fields(self) -> tuple[Locator, Locator, Locator, Locator]:
        return self.iframe_name, self.iframe_email, self.iframe_role, self.iframe_message_input

    def add_item(self) -> None:
        self.add_item_button.click()

    def remove_last_item(self) -> None:
        self.remove_item_button.click()

    def load_data(self) -> None:
        self.load_data_button.click()

    def set_custom_delay(self, delay_ms: int) -> None:
        self.delay_input.fill(str(delay_ms))

    def load_data_with_custom_delay(self) -> None:
        self.custom_delay_button.click()

    def select_tab(self, tab: str) -> None:
        self.get_tab_button(tab).click()

    def submit_iframe_form(self) -> None:
        self.iframe_submit_button.click()

    def clear_iframe_form(self) -> None:
        self.iframe_clear_button.click()

    def get_iframe_form_message(self) -> Locator:
        return self.iframe_form_message

    def toggle_iframe_text(self) -> None:
        self.iframe_text_toggle_button.click()

    def fill_iframe_form(self, name: str, email: str, role: str, message: str) -> None:
        self.iframe_name.fill(name)
        self.iframe_email.fill(email)
        self.iframe_role.select_option(role.lower())
        self.iframe_message_input.fill(message)
