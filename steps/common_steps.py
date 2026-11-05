from pytest_bdd import when, parsers
from pages.base_page import BasePage


@when(parsers.parse('user clicks to button with text "{text}"'))
def click_to_button_with_text(base_page: BasePage, text: str) -> None:
    base_page.click_to_button_with_text(text)

@when(parsers.parse('user double clicks to button with text "{text}"'))
def double_click_to_button_with_text(base_page: BasePage, text: str) -> None:
    base_page.click_to_button_with_text(text, is_double_click=True)
