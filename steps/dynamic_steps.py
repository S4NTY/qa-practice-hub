import re
import pytest
from playwright.sync_api import expect
from pytest_bdd import given, scenarios, then, when, parsers
from pages.dinamic_page import DynamicPage

scenarios("../features/dynamic.feature")


@pytest.fixture
def dynamic_page(page) -> DynamicPage:
    return DynamicPage(page)


@given("user opens dynamic page")
def open_dynamic_page(dynamic_page: DynamicPage) -> None:
    dynamic_page.open()

@when("user adds a new item to the dynamic list")
def add_item_to_dynamic_list(dynamic_page: DynamicPage) -> None:
    dynamic_page.add_item()

@when("user removes the last item from the dynamic list")
def remove_last_item_from_dynamic_list(dynamic_page: DynamicPage) -> None:
    dynamic_page.remove_last_item()

@when("user clicks the Load Data button")
def click_load_data_button(dynamic_page: DynamicPage) -> None:
    dynamic_page.load_data()

@then(parsers.parse('dynamic list contains "{items}"'))
def dynamic_list_contains(dynamic_page: DynamicPage, items: str) -> None:
    expected_items = [item.strip() for item in items.split(",")]
    expect(dynamic_page.get_dynamic_items()).to_have_text(expected_items)

@then("data loading spinner is visible")
def data_loading_spinner_is_visible(dynamic_page: DynamicPage) -> None:
    expect(dynamic_page.get_loading_spinner()).to_be_visible()

@then("loaded data is displayed")
def loaded_data_is_displayed(dynamic_page: DynamicPage) -> None:
    expect(dynamic_page.get_loaded_data()).to_have_text(re.compile(r"^Data loaded at .+"))
    expect(dynamic_page.get_loading_spinner()).to_be_hidden()

@when(parsers.parse("user sets custom delay to {delay_ms:d} ms"))
def set_custom_delay(dynamic_page: DynamicPage, delay_ms: int) -> None:
    dynamic_page.set_custom_delay(delay_ms)

@when("user loads data with custom delay")
def load_data_with_custom_delay(dynamic_page: DynamicPage) -> None:
    dynamic_page.load_data_with_custom_delay()

@then(parsers.parse('custom delay result equals "{message}"'))
def custom_delay_result_equals(dynamic_page: DynamicPage, message: str) -> None:
    expect(dynamic_page.get_custom_delay_result()).to_have_text(message)

@when(parsers.parse('user selects the "{tab}" tab'))
def select_tab(dynamic_page: DynamicPage, tab: str) -> None:
    dynamic_page.select_tab(tab)

@then(parsers.parse('the "{tab}" tab displays "{content}"'))
def tab_displays_content(dynamic_page: DynamicPage, tab: str, content: str) -> None:
    expect(dynamic_page.get_tab_button(tab)).to_have_class(re.compile(r"\bactive\b"))
    expect(dynamic_page.get_tab_panel(tab)).to_be_visible()
    expect(dynamic_page.get_tab_panel(tab)).to_have_text(content)
    for other_tab in {"Home", "Profile", "Settings"} - {tab}:
        expect(dynamic_page.get_tab_panel(other_tab)).to_be_hidden()

@when(parsers.parse('user fills the iframe form with name "{name}", email "{email}", role "{role}", and message "{message}"'))
def fill_iframe_form(dynamic_page: DynamicPage, name: str, email: str, role: str, message: str) -> None:
    dynamic_page.fill_iframe_form(name, email, role, message)

@when("user submits the iframe form")
def submit_iframe_form(dynamic_page: DynamicPage) -> None:
    dynamic_page.submit_iframe_form()

@when("user clicks Clear in the iframe form")
def clear_iframe_form(dynamic_page: DynamicPage) -> None:
    dynamic_page.clear_iframe_form()

@when("user clicks the iframe text toggle")
def toggle_iframe_text(dynamic_page: DynamicPage) -> None:
    dynamic_page.toggle_iframe_text()

@then(parsers.parse('iframe form message equals "{message}"'))
def iframe_form_message_equals(dynamic_page: DynamicPage, message: str) -> None:
    expect(dynamic_page.get_iframe_form_message()).to_be_visible()
    expect(dynamic_page.get_iframe_form_message()).to_have_text(message)

@then("iframe form fields are empty")
def iframe_form_fields_are_empty(dynamic_page: DynamicPage) -> None:
    for field in dynamic_page.get_iframe_form_fields():
        expect(field).to_have_value("")

@then("iframe form message is hidden")
def iframe_form_message_is_hidden(dynamic_page: DynamicPage) -> None:
    expect(dynamic_page.get_iframe_form_message()).to_be_hidden()

@then("iframe hidden text is visible")
def iframe_hidden_text_is_visible(dynamic_page: DynamicPage) -> None:
    expect(dynamic_page.get_iframe_hidden_text()).to_be_visible()

@then("iframe hidden text is hidden")
def iframe_hidden_text_is_hidden(dynamic_page: DynamicPage) -> None:
    expect(dynamic_page.get_iframe_hidden_text()).to_be_hidden()
