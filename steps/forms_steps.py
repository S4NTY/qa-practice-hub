import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from pages import FormPage
from steps.common_steps import *

scenarios("../features/forms.feature")


@pytest.fixture
def forms_page(page):
    return FormPage(page)


@given("user opens forms page")
def open_login_page(forms_page: FormPage) -> None:
    forms_page.open()

@when(parsers.parse('user enters login "{username}" and password "{password}" to login form'))
def enters_to_username_field(forms_page: FormPage, username: str, password: str) -> None:
    forms_page.login_username_input_set_text(username)
    forms_page.login_password_input_set_text(password)

@then(parsers.parse('login message equals "{message}"'))
def login_message_field_equals_message(forms_page: FormPage, message: str) -> None:
    expect(forms_page.get_login_message_label()).to_have_text(message)

@when(parsers.re(r'user enters "(?P<username>.*)" to username field on forgot password form'))
def enters_to_forgot_password_field(forms_page: FormPage, username: str) -> None:
    forms_page.forgot_username_input_set_text(username)

@then(parsers.parse('forgot password result equals "{message}"'))
def forgot_password_result_equals_message(forms_page: FormPage, message: str) -> None:
    expect(forms_page.get_forgot_password_result_label()).to_have_text(message)

@then(parsers.parse('forgot password message equals "{message}"'))
def forgot_password_message_equals_message(forms_page: FormPage, message: str) -> None:
    expect(forms_page.get_forgot_password_message_label()).to_have_text(message)

@when(parsers.re(r'user enters "(?P<first_name>.*)" to the first name field'))
def enters_to_reg_firstname_field(forms_page: FormPage, first_name: str) -> None:
    forms_page.reg_firstname_input_set_text(first_name)

@when(parsers.re(r'user enters "(?P<last_name>.*)" to the last name field'))
def enters_to_reg_lastname_field(forms_page: FormPage, last_name: str) -> None:
    forms_page.reg_lastname_input_set_text(last_name)

@when(parsers.re(r'user enters "(?P<email>.*)" to the email field'))
def enters_to_reg_email_field(forms_page: FormPage, email: str) -> None:
    forms_page.reg_email_input_set_text(email)

@when(parsers.parse('user selects country "{country}"'))
def select_reg_country(forms_page: FormPage, country: str) -> None:
    forms_page.reg_country_select_by_text(country)

@then(parsers.parse('register message equals "{message}"'))
def register_message_equals_message(forms_page: FormPage, message: str) -> None:
    expect(forms_page.get_reg_message_label()).to_have_text(message)

@then("registration form is empty")
def registration_form_is_empty(forms_page: FormPage) -> None:
    assert forms_page.is_registration_form_empty(), "Registration form is not empty"
