import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages import InputsPage
from steps.common_steps import *

scenarios("../features/inputs.feature")


@pytest.fixture
def inputs_page(page) -> InputsPage:
    return InputsPage(page)


@given("user opens inputs page")
def open_inputs_page(inputs_page: InputsPage) -> None:
    inputs_page.open()

@when(parsers.parse('user enters "{text}" in text input'))
def enter_text(inputs_page: InputsPage, text: str) -> None:
    inputs_page.get_text_input().fill(text)

@when("user clears text input")
def clear_text(inputs_page: InputsPage) -> None:
    inputs_page.get_text_input().clear()

@then(parsers.parse('text input value equals "{text}"'))
def text_input_value_equals(inputs_page: InputsPage, text: str) -> None:
    expect(inputs_page.get_text_input()).to_have_value(text)

@then("text input is empty")
def text_input_is_empty(inputs_page: InputsPage) -> None:
    expect(inputs_page.get_text_input()).to_have_value("")

@when(parsers.parse('user enters "{email}" in email input'))
def enter_email(inputs_page: InputsPage, email: str) -> None:
    inputs_page.get_email_input().fill(email)

@then(parsers.parse('email input value equals "{email}"'))
def email_input_value_equals(inputs_page: InputsPage, email: str) -> None:
    expect(inputs_page.get_email_input()).to_have_value(email)

@when("user shows password")
def show_password(inputs_page: InputsPage) -> None:
    inputs_page.get_password_toggle_button().click()

@when("user shows and hides password")
def show_and_hide_password(inputs_page: InputsPage) -> None:
    password_toggle_button = inputs_page.get_password_toggle_button()
    password_toggle_button.click()
    password_toggle_button.click()

@then(parsers.parse('password input type equals "{input_type}"'))
def password_input_type_equals(inputs_page: InputsPage, input_type: str) -> None:
    expect(inputs_page.get_password_input()).to_have_attribute("type", input_type)

@when(parsers.parse("user enters {number:d} in number input"))
def enter_number(inputs_page: InputsPage, number: int) -> None:
    inputs_page.get_number_input().fill(str(number))

@then(parsers.parse('number input value equals "{number}"'))
def number_input_value_equals(inputs_page: InputsPage, number: str) -> None:
    expect(inputs_page.get_number_input()).to_have_value(number)

@when(parsers.parse('user enters "{date}" in date input'))
def enter_date(inputs_page: InputsPage, date: str) -> None:
    inputs_page.get_date_input().fill(date)

@then(parsers.parse('date input value equals "{date}"'))
def date_input_value_equals(inputs_page: InputsPage, date: str) -> None:
    expect(inputs_page.get_date_input()).to_have_value(date)

@when(parsers.parse('user enters "{time}" in time input'))
def enter_time(inputs_page: InputsPage, time: str) -> None:
    inputs_page.get_time_input().fill(time)

@then(parsers.parse('time input value equals "{time}"'))
def time_input_value_equals(inputs_page: InputsPage, time: str) -> None:
    expect(inputs_page.get_time_input()).to_have_value(time)

@when(parsers.parse('user enters "{query}" in search input'))
def enter_search_query(inputs_page: InputsPage, query: str) -> None:
    inputs_page.get_search_input().fill(query)

@then(parsers.parse('search input value equals "{query}"'))
def search_input_value_equals(inputs_page: InputsPage, query: str) -> None:
    expect(inputs_page.get_search_input()).to_have_value(query)

@when(parsers.parse('user selects phone country "{country_code}"'))
def select_phone_country(inputs_page: InputsPage, country_code: str) -> None:
    inputs_page.get_phone_country_button().click()
    inputs_page.get_phone_country_option(country_code).click()

@then(parsers.parse('phone country code equals "{country_code}"'))
def phone_country_code_equals(inputs_page: InputsPage, country_code: str) -> None:
    expect(inputs_page.get_phone_prefix()).to_have_text(country_code)

@when(parsers.parse('user enters "{phone}" in phone input'))
def enter_phone(inputs_page: InputsPage, phone: str) -> None:
    inputs_page.get_phone_input().fill(phone)

@then(parsers.parse('phone input value equals "{phone}"'))
def phone_input_value_equals(inputs_page: InputsPage, phone: str) -> None:
    expect(inputs_page.get_phone_input()).to_have_value(phone)

@when(parsers.parse('user enters "{text}" in textarea'))
def enter_textarea_text(inputs_page: InputsPage, text: str) -> None:
    inputs_page.get_textarea().fill(text)

@then(parsers.parse('textarea value equals "{text}"'))
def textarea_value_equals(inputs_page: InputsPage, text: str) -> None:
    expect(inputs_page.get_textarea()).to_have_value(text)

@when("user focuses read-only input")
def focus_readonly_input(inputs_page: InputsPage) -> None:
    inputs_page.get_readonly_input().focus()

@then(parsers.parse('read-only input value equals "{text}" and is read-only'))
def readonly_input_is_unchanged_and_readonly(inputs_page: InputsPage, text: str) -> None:
    expect(inputs_page.get_readonly_input()).to_have_value(text)
    expect(inputs_page.get_readonly_input()).not_to_be_editable()

@when("user views disabled input")
def view_disabled_input(inputs_page: InputsPage) -> None:
    inputs_page.get_disabled_input().scroll_into_view_if_needed()

@then(parsers.parse('disabled input value equals "{text}" and is disabled'))
def disabled_input_is_unchanged_and_disabled(inputs_page: InputsPage, text: str) -> None:
    expect(inputs_page.get_disabled_input()).to_have_value(text)
    expect(inputs_page.get_disabled_input()).to_be_disabled()

@when(parsers.parse('user enters "{text}" in live output input'))
def enter_live_output_text(inputs_page: InputsPage, text: str) -> None:
    inputs_page.get_live_output_input().fill(text)

@then(parsers.parse('live output equals "{text}"'))
def live_output_equals(inputs_page: InputsPage, text: str) -> None:
    expect(inputs_page.get_live_output()).to_have_text(text)
