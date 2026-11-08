from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class ButtonsGoAheadPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._ahead_page_title = page.get_by_test_id("ahead-page-title")
        self._go_back_previous_button = page.get_by_test_id("btn-go-back-previous")
        self._go_back_main_button = page.get_by_test_id("btn-go-back-main")


    def open(self) -> None:
        super().open("ahead-page")

    def get_ahead_page_title(self) -> Locator:
        return self._ahead_page_title

    def go_back_previous_button_click(self):
        from pages.buttons_next_page import ButtonsNextPage
        self._go_back_previous_button.click()
        return ButtonsNextPage(page=self.page)

    def go_back_main_page_click(self):
        self._go_back_main_button.click()
        return BasePage(page=self.page)
