from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class DynamicPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._add_item_button = page.get_by_test_id("btn-add-element")
        self._dynamic_items = page.get_by_test_id("dynamic-list").locator("li")
        self._remove_item_button = page.get_by_test_id("btn-remove-element")
        self._load_data_button = page.get_by_test_id("btn-load-data")
        self._loading_spinner = page.get_by_test_id("loading-spinner")
        self._loaded_data = page.get_by_test_id("loaded-data")
        self._delay_input = page.get_by_test_id("delay-input")
        self._custom_delay_button = page.get_by_test_id("btn-custom-delay")
        self._custom_delay_result = page.get_by_test_id("custom-delay-result")
        self._practice_frame = page.frame_locator('[data-testid="practice-iframe"]')
        self._iframe_name = self._practice_frame.get_by_test_id("iframe-name")
        self._iframe_email = self._practice_frame.get_by_test_id("iframe-email")
        self._iframe_role = self._practice_frame.get_by_test_id("iframe-role")
        self._iframe_message_input = self._practice_frame.get_by_test_id("iframe-message")
        self._iframe_submit_button = self._practice_frame.get_by_test_id("iframe-submit")
        self._iframe_clear_button = self._practice_frame.get_by_test_id("iframe-clear")
        self._iframe_form_message = self._practice_frame.get_by_test_id("iframe-message-box")
        self._iframe_text_toggle_button = self._practice_frame.get_by_test_id("iframe-toggle-text")
        self._iframe_hidden_text = self._practice_frame.get_by_test_id("iframe-hidden-text")


    def open(self) -> None:
        super().open("#dynamic")

    def get_dynamic_items(self) -> Locator:
        return self._dynamic_items

    def get_loading_spinner(self) -> Locator:
        return self._loading_spinner

    def get_custom_delay_result(self) -> Locator:
        return self._custom_delay_result

    def get_tab_button(self, tab: str) -> Locator:
        return self.page.get_by_test_id(f"tab-btn-{tab.lower()}")

    def get_tab_panel(self, tab: str) -> Locator:
        return self.page.get_by_test_id(f"tab-panel-{tab.lower()}")

    def get_loaded_data(self) -> Locator:
        return self._loaded_data

    def get_iframe_hidden_text(self) -> Locator:
        return self._iframe_hidden_text

    def get_iframe_form_fields(self) -> tuple[Locator, Locator, Locator, Locator]:
        return self._iframe_name, self._iframe_email, self._iframe_role, self._iframe_message_input

    def add_item(self) -> None:
        self._add_item_button.click()

    def remove_last_item(self) -> None:
        self._remove_item_button.click()

    def load_data(self) -> None:
        self._load_data_button.click()

    def set_custom_delay(self, delay_ms: int) -> None:
        self._delay_input.fill(str(delay_ms))

    def load_data_with_custom_delay(self) -> None:
        self._custom_delay_button.click()

    def select_tab(self, tab: str) -> None:
        self.get_tab_button(tab).click()

    def submit_iframe_form(self) -> None:
        self._iframe_submit_button.click()

    def clear_iframe_form(self) -> None:
        self._iframe_clear_button.click()

    def get_iframe_form_message(self) -> Locator:
        return self._iframe_form_message

    def toggle_iframe_text(self) -> None:
        self._iframe_text_toggle_button.click()

    def fill_iframe_form(self, name: str, email: str, role: str, message: str) -> None:
        self._iframe_name.fill(name)
        self._iframe_email.fill(email)
        self._iframe_role.select_option(role.lower())
        self._iframe_message_input.fill(message)
