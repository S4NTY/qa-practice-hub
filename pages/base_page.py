from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://qapracticehub.com"

    def open(self, path: str = "") -> None:
        self.page.goto(f"{self.base_url}/{path}")

    def get_title(self) -> str:
        return self.page.title()

    def should_have_url(self, url: str):
        expect(self.page).to_have_url(url)

    def click_to_button_with_text(self, text: str) -> None:
        self.page.get_by_role("button", name=text).click()

    def close(self):
        self.page.close()