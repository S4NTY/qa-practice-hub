import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when
from pages import PracticeLabPage

scenarios("../features/practice_lab.feature")


@pytest.fixture
def practice_lab_page(page) -> PracticeLabPage:
    return PracticeLabPage(page)


@given("user opens Practice Lab page")
def open_practice_lab_page(practice_lab_page: PracticeLabPage) -> None:
    practice_lab_page.open()

@given(parsers.parse('wizard personal details are "{name}" and "{email}"'))
@when(parsers.parse('user enters wizard personal details "{name}" and "{email}"'))
def enter_wizard_personal_details(
    practice_lab_page: PracticeLabPage, name: str, email: str
) -> None:
    practice_lab_page.enter_wizard_personal_details(name, email)

@given(parsers.parse('wizard address details are "{city}" and "{zip_code}"'))
@when(parsers.parse('user enters wizard address "{city}" and "{zip_code}"'))
def enter_wizard_address(
    practice_lab_page: PracticeLabPage, city: str, zip_code: str
) -> None:
    practice_lab_page.enter_wizard_address(city, zip_code)

@given("user proceeds to the next wizard step")
@when("user proceeds to the next wizard step")
def proceed_to_next_wizard_step(practice_lab_page: PracticeLabPage) -> None:
    practice_lab_page.go_to_next_wizard_step()

@given("user returns to the previous wizard step")
@when("user returns to the previous wizard step")
def return_to_previous_wizard_step(practice_lab_page: PracticeLabPage) -> None:
    practice_lab_page.go_to_previous_wizard_step()

@when("user submits the wizard")
def submit_wizard(practice_lab_page: PracticeLabPage) -> None:
    practice_lab_page.submit_wizard()

@when(parsers.parse('user selects date "{date_text}" in the custom date picker'))
def select_custom_date(practice_lab_page: PracticeLabPage, date_text: str) -> None:
    practice_lab_page.select_custom_date(date_text)

@when(parsers.parse("user clicks the stale demo button {times:d} times"))
def click_stale_demo_button(practice_lab_page: PracticeLabPage, times: int) -> None:
    practice_lab_page.click_stale_demo(times)

@then(parsers.parse('wizard message equals "{message}"'))
def wizard_message_equals(practice_lab_page: PracticeLabPage, message: str) -> None:
    expect(practice_lab_page.get_wizard_message()).to_have_text(message)

@then(parsers.parse("wizard step {step:d} is visible"))
def wizard_step_is_visible(practice_lab_page: PracticeLabPage, step: int) -> None:
    expect(practice_lab_page.get_wizard_panel(step)).to_be_visible()

@then(
    parsers.parse(
        'wizard review contains name "{name}", email "{email}", '
        'city "{city}" and ZIP "{zip_code}"'
    )
)
def wizard_review_contains_details(
    practice_lab_page: PracticeLabPage,
    name: str,
    email: str,
    city: str,
    zip_code: str,
) -> None:
    review = practice_lab_page.get_wizard_review()
    expect(review).to_contain_text(f"Name: {name}")
    expect(review).to_contain_text(f"Email: {email}")
    expect(review).to_contain_text(f"City: {city}")
    expect(review).to_contain_text(f"ZIP: {zip_code}")

@then(parsers.parse('wizard personal fields contain "{name}" and "{email}"'))
def wizard_personal_fields_contain(
    practice_lab_page: PracticeLabPage, name: str, email: str
) -> None:
    expect(practice_lab_page.get_wizard_name_input()).to_have_value(name)
    expect(practice_lab_page.get_wizard_email_input()).to_have_value(email)

@then("wizard form fields are empty")
def wizard_form_fields_are_empty(practice_lab_page: PracticeLabPage) -> None:
    expect(practice_lab_page.get_wizard_name_input()).to_have_value("")
    expect(practice_lab_page.get_wizard_email_input()).to_have_value("")
    expect(practice_lab_page.get_wizard_city_input()).to_have_value("")
    expect(practice_lab_page.get_wizard_zip_input()).to_have_value("")

@then(parsers.parse('custom date output message equals "{message}"'))
def custom_date_output_message_equals(
    practice_lab_page: PracticeLabPage, message: str
) -> None:
    expect(practice_lab_page.get_custom_date_output()).to_have_text(message)

@then("custom date picker is closed")
def custom_date_picker_is_closed(practice_lab_page: PracticeLabPage) -> None:
    expect(practice_lab_page.get_custom_date_picker()).to_be_hidden()

@then(parsers.parse('custom date field shows "{date_text}"'))
def custom_date_field_shows(practice_lab_page: PracticeLabPage, date_text: str) -> None:
    expect(practice_lab_page.get_custom_date_value()).to_have_text(date_text)
    expect(practice_lab_page.get_custom_date_input()).to_have_value(date_text)

@then(parsers.parse('stale demo output equals "{message}"'))
def stale_demo_output_equals(practice_lab_page: PracticeLabPage, message: str) -> None:
    expect(practice_lab_page.get_stale_demo_output()).to_have_text(message)

@then(parsers.parse("stale demo button render version is {version:d}"))
def stale_demo_button_render_version(
    practice_lab_page: PracticeLabPage, version: int
) -> None:
    expect(practice_lab_page.get_stale_demo_button()).to_have_attribute(
        "data-render-version", str(version)
    )
