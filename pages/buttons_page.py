from pages.base_page import BasePage
from playwright.sync_api import Page, Locator
from pages.buttons_next_page import ButtonsNextPage


class ButtonsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.button_output_label = page.get_by_test_id("button-output")
        self.counter_button = page.get_by_test_id("btn-click-counter")
        self.right_click_button = page.get_by_test_id("btn-right-click")
        self.hover_button = page.get_by_test_id("btn-hover")
        self.next_page_button = page.get_by_test_id("btn-next-page")
        self.download_button = page.get_by_test_id("btn-download")
        self.buttons_popup_overlay = page.get_by_test_id("buttons-popup-overlay")
        self.buttons_popup_close_button = page.get_by_test_id("buttons-popup-close")
        self.info_click_button = page.get_by_test_id("info-btn-click")
        self.info_click_popup = page.get_by_test_id("info-popup-click")
        self.info_hover_button = page.get_by_test_id("info-btn-hover")
        self.info_hover_popup = page.get_by_test_id("info-popup-hover")


    def open(self) -> None:
        super().open("#buttons")

    def get_button_output_label(self) -> Locator:
        return self.button_output_label

    def get_counter_button(self) -> Locator:
        return self.counter_button

    def get_buttons_popup_overlay(self) -> Locator:
        return self.buttons_popup_overlay

    def get_info_click_button(self) -> Locator:
        return self.info_click_button

    def get_info_click_popup(self) -> Locator:
        return self.info_click_popup

    def get_info_hover_button(self) -> Locator:
        return self.info_hover_button

    def get_info_hover_popup(self) -> Locator:
        return self.info_hover_popup

    def right_click_button_click(self) -> None:
        self.right_click_button.click(button="right")

    def hover_button_hover(self) -> None:
        self.hover_button.hover()

    def next_page_click(self) -> ButtonsNextPage:
        self.next_page_button.click()
        return ButtonsNextPage(page=self.page)

    def download_sample_file(self):
        with self.page.expect_download() as download_info:
            self.download_button.click()
        return download_info.value

    def close_buttons_popup(self) -> None:
        self.buttons_popup_close_button.click()

    def info_click_button_click(self) -> None:
        self.info_click_button.click()

    def info_hover_button_hover(self) -> None:
        self.info_hover_button.hover()

    def move_mouse_away(self) -> None:
        self.page.mouse.move(0, 0)
