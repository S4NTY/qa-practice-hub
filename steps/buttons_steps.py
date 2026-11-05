import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from pages import ButtonsPage, ButtonsNextPage, ButtonsGoAheadPage
from steps.common_steps import *

scenarios("../features/buttons.feature")


@pytest.fixture
def buttons_page(page):
    return ButtonsPage(page)


@given("user opens buttons page")
def open_buttons_page(buttons_page: ButtonsPage) -> None:
    buttons_page.open()

@then(parsers.parse('button output message equals "{message}"'))
def button_output_message_equals(buttons_page: ButtonsPage, message: str) -> None:
    expect(buttons_page.get_button_output_label()).to_have_text(message)

@when('user clicks to "Right Click Me" button')
def right_clicks_to_button(buttons_page: ButtonsPage) -> None:
    buttons_page.right_click_button_click()

@when("user hover to hover button")
def hover_button_hover(buttons_page: ButtonsPage) -> None:
    buttons_page.hover_button_hover()

@when('user clicks to "Next Page" button', target_fixture="buttons_next_page")
def next_page_button_click(buttons_page: ButtonsPage) -> ButtonsNextPage:
    return buttons_page.next_page_click()

@then("buttons next page is opened")
def buttons_next_page_is_opened(buttons_next_page: ButtonsNextPage) -> None:
    buttons_next_page.should_have_url("https://qapracticehub.com/next-page")
    expect(buttons_next_page.get_next_page_title()).to_have_text("Successfully landed on the new page")

@when('user clicks to "Go Back" button', target_fixture="base_page")
def go_back_button_click(buttons_next_page: ButtonsNextPage) -> BasePage:
    return buttons_next_page.go_back_button_click()

@then("main page is opened")
def buttons_page_is_opened(base_page: BasePage) -> None:
    base_page.should_have_url(base_page.base_url)

@when('user clicks to "Go Ahead" button', target_fixture="buttons_go_ahead_page")
def go_ahead_button_click(buttons_next_page: ButtonsNextPage) -> ButtonsGoAheadPage:
    return buttons_next_page.go_ahead_button_click()

@then("buttons ahead page is opened")
def buttons_ahead_page_is_opened(buttons_go_ahead_page: ButtonsGoAheadPage) -> None:
    buttons_go_ahead_page.should_have_url("https://qapracticehub.com/ahead-page")
    expect(buttons_go_ahead_page.get_ahead_page_title()).to_have_text("Successfully landed on the ahead page")

@when('user clicks to "Go Back to Previous Page" button', target_fixture="buttons_next_page")
def go_back_previous_button_click(buttons_go_ahead_page: ButtonsGoAheadPage) -> ButtonsNextPage:
    return buttons_go_ahead_page.go_back_previous_button_click()

@when('user clicks to "Go Back to Main Page" button', target_fixture="base_page")
def go_ahead_button_click(buttons_go_ahead_page: ButtonsGoAheadPage) -> BasePage:
    return buttons_go_ahead_page.go_back_main_page_click()

@when('user clicks to "Download Sample File" button', target_fixture="downloaded_file")
def download_sample_file(buttons_page: ButtonsPage):
    return buttons_page.download_sample_file()

@then(parsers.parse('downloaded file name is "{file_name}"'))
def check_download_filename(downloaded_file, file_name: str) -> None:
    assert downloaded_file.suggested_filename == file_name

@then(parsers.parse('downloaded file content is "{expected_content}"'))
def check_download_content(downloaded_file, expected_content: str) -> None:
    content = downloaded_file.path().read_text(encoding="utf-8")
    expected = expected_content.replace("\\n", "\n")
    assert content.strip() == expected.strip()

@then(parsers.re("buttons selection popup is (?P<state>visible|hidden)"))
def buttons_selection_popup_state(buttons_page: ButtonsPage, state: str) -> None:
    expect(buttons_page.get_buttons_popup_overlay()).to_be_visible(visible=(state == "visible"))

@when('user close buttons selection popup')
def close_buttons_selection_popup(buttons_page: ButtonsPage) -> None:
    buttons_page.close_buttons_popup()

@when('user clicks to "Click Info" button')
def info_click_button_click(buttons_page: ButtonsPage):
    expect(buttons_page.get_info_click_button()).to_be_visible()
    buttons_page.info_click_button_click()

@then(parsers.re("info popup click is (?P<state>visible|hidden)"))
def buttons_info_popup_click_state(buttons_page: ButtonsPage, state: str) -> None:
    expect(buttons_page.get_info_click_popup()).to_be_visible(visible=(state == "visible"))

@when('user hover to "Hover Info" button')
def info_hover_button_hover(buttons_page: ButtonsPage):
    expect(buttons_page.get_info_hover_button()).to_be_visible()
    buttons_page.info_hover_button_hover()

@then(parsers.re("info popup hover is (?P<state>visible|hidden)"))
def buttons_info_popup_hover_state(buttons_page: ButtonsPage, state: str) -> None:
    expect(buttons_page.get_info_hover_popup()).to_be_visible(visible=(state == "visible"))

@when("user moves mouse away from hover info button")
def move_mouse_away(buttons_page: ButtonsPage) -> None:
    buttons_page.move_mouse_away()
