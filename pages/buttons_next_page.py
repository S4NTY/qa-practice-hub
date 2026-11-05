from pages.base_page import BasePage
from pages.buttons_go_ahead_page import ButtonsGoAheadPage
from playwright.sync_api import Page, Locator


class ButtonsNextPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.next_page_title = page.get_by_test_id("next-page-title")
        self.go_back_button = page.get_by_test_id("btn-go-back")
        self.go_ahead_button = page.get_by_test_id("btn-go-ahead")


    def open(self) -> None:
        super().open("next-page")

    def get_next_page_title(self) -> Locator:
        return self.next_page_title

    def go_back_button_click(self):
        self.go_back_button.click()
        return BasePage(page=self.page)

    def go_ahead_button_click(self):
        self.go_ahead_button.click()
        return ButtonsGoAheadPage(page=self.page)
